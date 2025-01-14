from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime

# Inicializa o cliente Supabase para comunicação com o banco de dados
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class HistoricoRefeicao:
    """
    Classe responsável por gerenciar o histórico de refeições, incluindo o armazenamento e a exibição
    das informações de nutrientes e insulina associadas.
    """

    def salvaRefeicao(self, usuario: str, refeicao: str, nutrientes: list, insulina: float) -> bool:
        """
        Salva as informações de uma refeição no banco de dados.
        """
        # Obtém o ID da refeição com base no nome
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
        id_refeicao = resposta_refeicao.data[0]['id'] if resposta_refeicao.data else None

        # Obtém o ID do usuário com base no e-mail
        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()
        id_usuario = resposta_usuario.data[0]['id'] if resposta_usuario.data else None

        # Verifica se os IDs necessários foram encontrados
        if not (id_refeicao and id_usuario):
            print("Erro ao localizar refeição ou usuário no banco de dados.")
            return False

        # Define a data atual para a refeição
        dia_refeicao = datetime.today().strftime('%Y-%m-%d')

        # Insere os dados da refeição no banco
        response = supabase.table('Historico').insert({
            'dia': dia_refeicao,
            'id_refeicao': id_refeicao,
            'energia': nutrientes[0],
            'proteina': nutrientes[1],
            'lipideo': nutrientes[2],
            'carboidrato': nutrientes[3],
            'fibra': nutrientes[4],
            'insulina': insulina,
            'id_usuario': id_usuario
        }).execute()

        # Verifica se a operação foi bem-sucedida
        if not response.data:
            print("Erro ao salvar a refeição no histórico.")
            return False

        return True

    def mostraHistorico(self, data: str, refeicao: str, usuario: str) -> str:
        """
        Recupera e exibe o histórico de uma refeição específica em uma data fornecida.
        """
        # Obtém o ID da refeição
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
        id_refeicao = resposta_refeicao.data[0]['id'] if resposta_refeicao.data else None

        # Obtém o ID do usuário
        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()
        id_usuario = resposta_usuario.data[0]['id'] if resposta_usuario.data else None

        # Verifica se os IDs necessários foram encontrados
        if not (id_refeicao and id_usuario):
            print("Erro ao localizar refeição ou usuário no banco de dados.")
            return "Histórico indisponível."

        # Consulta o histórico da refeição para a data e usuário fornecidos
        response = supabase.table("Historico").select(
            "dia, Refeicao(refeicao), proteina, carboidrato, fibra, lipideo, energia, insulina"
        ).match({"dia": data, "id_refeicao": id_refeicao, "id_usuario": id_usuario}).execute()

        dados = response.data
        if not dados:
            return "Nenhum dado encontrado no histórico para a data e refeição especificadas."

        # Limita a exibição ao primeiro item para simplificação
        dados_limitados = dados[:1]

        # Formata os dados para exibição
        linhas_formatadas = []
        for item in dados_limitados:
            linhas_formatadas.append(f"{refeicao}:")
            linhas_formatadas.append(f"  Proteína: {item['proteina']} g")
            linhas_formatadas.append(f"  Carboidrato: {item['carboidrato']} g")
            linhas_formatadas.append(f"  Fibra: {item['fibra']} g")
            linhas_formatadas.append(f"  Lipídeo: {item['lipideo']} g")
            linhas_formatadas.append(f"  Energia: {item['energia']} kcal")
            linhas_formatadas.append(f"  Dosagem Insulina: {item['insulina']} U")
            linhas_formatadas.append("-" * 40)

        return "\n".join(linhas_formatadas)
