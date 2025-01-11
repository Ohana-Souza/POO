from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class HistoricoRefeicao:
    def salvaRefeicao(self, usuario_email, refeicao, descricao, nutrientes):
        """
        Salva uma refeição no histórico associada a um usuário, alimento e nutrientes.

        Args:
            usuario_email (str): Email do usuário autenticado.
            refeicao (str): Tipo de refeição (ex: "Café da manhã").
            descricao (str): Descrição do alimento.
            nutrientes (list): Lista com valores de nutrientes (energia, proteína, lipídeo, carboidrato, fibra).

        Returns:
            bool: True se os dados foram salvos com sucesso, False caso contrário.
        """
        
        print(f"Email do usuário: {usuario_email}")
        print(f"Refeição: {refeicao}")
        print(f"Descrição do alimento: {descricao}")
        print(f"Nutrientes: {nutrientes}")

        # Busca o ID da refeição
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
        if not resposta_refeicao.data:
            print(f"Refeição '{refeicao}' não encontrada.")
            return False
        id_refeicao = resposta_refeicao.data[0]['id']

        # Busca o ID do alimento
        resposta_alimento = supabase.table('Alimentos').select('id').eq('descricao', descricao).execute()
        if not resposta_alimento.data:
            print(f"Alimento '{descricao}' não encontrado.")
            return False
        id_alimento = resposta_alimento.data[0]['id']

        # Busca o ID do usuário
        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario_email).execute()
        if not resposta_usuario.data:
            print(f"Usuário com email '{usuario_email}' não encontrado.")
            return False
        id_usuario = resposta_usuario.data[0]['id']

        # Data da refeição
        dia_refeicao = datetime.today().strftime('%Y-%m-%d')

        # Insere os dados no histórico
        response = supabase.table('Historico').insert({
            'dia': dia_refeicao,
            'id_refeicao': id_refeicao,
            'id_alimento': id_alimento,
            'energia': nutrientes[0],
            'proteina': nutrientes[1],
            'lipideo': nutrientes[2],
            'carboidrato': nutrientes[3],
            'fibra': nutrientes[4],
            'id_usuario': id_usuario
        }).execute()

        if not response.data:  # Verifica se a resposta contém dados
            print("Erro ao salvar no histórico. Nenhum dado foi inserido.")
            return False

        return True

    def mostraHistorico(self, data, refeicao, usuario_email):
        try:
            # Busca o ID da refeição
            resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
            if not resposta_refeicao.data:
                raise ValueError(f"Refeição '{refeicao}' não encontrada.")
            id_refeicao = resposta_refeicao.data[0]['id']

            # Busca o ID do usuário
            resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario_email).execute()
            if not resposta_usuario.data:
                raise ValueError(f"Usuário com email '{usuario_email}' não encontrado.")
            id_usuario = resposta_usuario.data[0]['id']

            # Consulta o histórico
            response = supabase.table("Historico").select(
                "dia, Refeicao(refeicao), Alimentos(descricao), proteina, carboidrato, fibra, lipideo, energia"
            ).match({
                "dia": data,
                "id_refeicao": id_refeicao,
                "id_usuario": id_usuario
            }).execute()

            if not response.data:  # Verifica se há dados na resposta
                print(f"Nenhum dado encontrado no histórico para {data}, refeição '{refeicao}'.")
                return False

            return response.data

        except Exception as e:
            print(f"Erro ao buscar histórico: {e}")
            return False

