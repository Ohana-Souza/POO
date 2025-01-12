from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime
from Alimento import Alimento

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class HistoricoAlimentos:
    def salvaAlimento(self, usuario, refeicao, descricao, nutrientes):
        print(f"Usuário: {usuario}, Refeição: {refeicao}, Descrição: {descricao}, Nutrientes: {nutrientes}")

        # Validar dados antes de prosseguir
        if not usuario or not refeicao or not descricao or not nutrientes:
            print("Erro: Dados insuficientes para salvar o alimento.")
            return False

        # Buscar IDs no banco
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
        if not resposta_refeicao.data:
            print("Erro: Refeição não encontrada no banco.")
            return False
        id_refeicao = resposta_refeicao.data[0]['id']

        resposta_alimento = supabase.table('Alimentos').select('id').eq('descricao', descricao).execute()
        if not resposta_alimento.data:
            print("Erro: Alimento não encontrado no banco.")
            return False
        id_alimento = resposta_alimento.data[0]['id']

        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()
        if not resposta_usuario.data:
            print("Erro: Usuário não encontrado no banco.")
            return False
        id_usuario = resposta_usuario.data[0]['id']

        # Inserir no banco
        dia_refeicao = datetime.today().strftime('%Y-%m-%d')
        
        response = supabase.table('Historico_Alimentos').insert({
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

        if response.data:
            print("Alimento salvo com sucesso.")
        else:
            print("Erro ao salvar alimento no banco:", response.get('error', 'Erro desconhecido'))
            
                

        if response.data:
            print("Alimento salvo com sucesso.")
            return True

        print("Erro ao salvar alimento no banco.", response.get('error', 'Erro desconhecido'))
        return False


    def mostraHistorico(self, data, refeicao, usuario):

        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()

        if resposta_refeicao.data and len(resposta_refeicao.data) > 0:
            id_refeicao = resposta_refeicao.data[0]['id']


        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()

        if resposta_usuario.data and len(resposta_usuario.data) > 0:
            id_usuario = resposta_usuario.data[0]['id']

        response = supabase.table("Historico_Alimentos").select(
    "dia, Alimentos(descricao), Refeicao(refeicao), proteina, carboidrato, fibra, lipideo, energia"
).match({"dia": data, "id_refeicao": id_refeicao, "id_usuario": id_usuario}).execute()

        dados = response.data

        linhas_formatadas = []

        for i, item in enumerate(dados, 1):
            linhas_formatadas.append(f"Alimento {i}:")
            linhas_formatadas.append(f"  Proteína: {item['proteina']} g")
            linhas_formatadas.append(f"  Carboidrato: {item['carboidrato']} g")
            linhas_formatadas.append(f"  Fibra: {item['fibra']} g")
            linhas_formatadas.append(f"  Lipídeo: {item['lipideo']} g")
            linhas_formatadas.append(f"  Energia: {item['energia']} kcal")
            linhas_formatadas.append("-" * 40)
        

        if not response.data:  
            print("Nenhum dado encontrado no histórico")
            return False

        if 'error' in response:  
            print("Erro ao buscar dados:", response['error'])
            return False

        return "\n".join(linhas_formatadas)


