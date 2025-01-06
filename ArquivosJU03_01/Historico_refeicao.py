from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime
from Alimento import Alimento

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class HistoricoRefeicao:
    
    def salvaRefeicao(self, refeicao, descricao, nutrientes):
        
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()

        if resposta_refeicao.data and len(resposta_refeicao.data) > 0:
            id_refeicao = resposta_refeicao.data[0]['id']
        else:
            print("Refeição não encontrada.")
            return False

        resposta_alimento = supabase.table('Alimentos').select('id').eq('descricao', descricao).execute()

        if resposta_alimento.data and len(resposta_alimento.data) > 0:
            id_alimento = resposta_alimento.data[0]['id']
        else:
            print("Alimento não encontrado.")
            return False

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

        if not response.data:
            print("Nenhum dado encontrado para o alimento selecionado.")
            return []

        if 'error' in response:
            print("Erro ao buscar dados:", response['error'])
            return False

        return True
    
    def obtemHistorico(self):
        response = supabase.table('Historico').select(
            'dia', 'id_refeicao(refeicao)', 'id_alimento(descricao)', 'energia', 'proteina', 'lipideo', 'carboidrato', 'fibra'
        ).execute()
        
        if not response.data:
            print("Nenhum dado encontrado.")
            return []

        if 'error' in response:
            print("Erro ao buscar dados:", response['error'])
            return []

        historico = []
        for item in response.data:
            historico.append(
                f"Data: {item['dia']}, Refeição: {item['id_refeicao']['refeicao']}, "
                f"Alimento: {item['id_alimento']['descricao']}, Energia: {item['energia']}kcal, "
                f"Proteína: {item['proteina']}g, Lipídeo: {item['lipideo']}g, "
                f"Carboidrato: {item['carboidrato']}g, Fibra: {item['fibra']}g"
            )
        return historico
