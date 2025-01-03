from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime
from Alimento import Alimento

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class HistoricoRefeicao:
    
    def salvaRefeicao(self, refeicao, descricao, nutrientes): # tem q receber Alimento.descricao e Alimento.nutrientes
        
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()

        if resposta_refeicao.data and len(resposta_refeicao.data) > 0:
            id_refeicao = resposta_refeicao.data[0]['id']

        resposta_alimento = supabase.table('Alimentos').select('id').eq('descricao', descricao).execute()

        if resposta_alimento.data and len(resposta_alimento.data) > 0:
            id_alimento = resposta_alimento.data[0]['id']

        
        dia_refeicao = datetime.today().strftime('%Y-%m-%d')

        response = supabase.table('Historico').insert({
            'dia': dia_refeicao,
            'id_refeicao': id_refeicao,
            'id_alimento': id_alimento,
            'energia' : nutrientes[0],
            'proteina': nutrientes[1],
            'lipideo': nutrientes[2],
            'carboidrato': nutrientes[3],
            'fibra': nutrientes[4],
        }).execute()


        if not response.data:  # If no data was returned
            print("Nenhum dado encontrado para o alimento selecionado.")
            return []

        if 'error' in response:  # Check if an error exists
            print("Erro ao buscar dados:", response['error'])
            return False

        

testeAl = Alimento()
testeAl.adicionaAlimento(1, 200)
teste = HistoricoRefeicao()
teste.salvaRefeicao("Café da manhã", testeAl.descricao, testeAl.nutrientes)



