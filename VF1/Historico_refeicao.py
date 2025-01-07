from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime
from Alimento import Alimento

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class HistoricoRefeicao:
    
    def salvaRefeicao(self, refeicao, descricao, nutrientes):
        # Obter ID da refeição
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
        if not resposta_refeicao.data:
            print(f"Refeição '{refeicao}' não encontrada no banco de dados.")
            return False
        id_refeicao = resposta_refeicao.data[0]['id']
        print(f"ID da Refeição: {id_refeicao}")

        # Obter ID do alimento
        resposta_alimento = supabase.table('Alimentos').select('id').eq('descricao', descricao).execute()
        if not resposta_alimento.data:
            print(f"Alimento '{descricao}' não encontrado no banco de dados.")
            return False
        id_alimento = resposta_alimento.data[0]['id']
        print(f"ID do Alimento: {id_alimento}")

        # Inserir no histórico
        dia_refeicao = datetime.today().strftime('%Y-%m-%d')
        response = supabase.table('Historico').insert({
            'dia': dia_refeicao,
            'id_refeicao': id_refeicao,
            'id_alimento': id_alimento,
            'energia': nutrientes[0],
            'proteina': nutrientes[1],
            'lipideo': nutrientes[2],
            'carboidrato': nutrientes[3],
            'fibra': nutrientes[4],
        }).execute()

        # Verificar se houve erro
        if not response.data:  # Caso nenhum dado tenha sido retornado
            print("Erro ao salvar no histórico: Nenhuma resposta do banco.")
            return False

        print("Inserção no histórico realizada com sucesso.")
        return True


    def mostraHistorico(self, data):
        response = supabase.table("Historico").select("dia, Refeicao(refeicao), Alimentos(descricao), proteina, carboidrato, fibra, lipideo, energia").eq("dia", data).execute()
        
        if not response.data:  
            print("Nenhum dado encontrado no histórico")
            return []

        if 'error' in response:  
            print("Erro ao buscar dados:", response['error'])
            return []

        return response.data
        


