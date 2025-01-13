from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime
from Alimento import Alimento

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class HistoricoAlimentos:
    
    def salvaAlimento(self, usuario, refeicao, descricao, nutrientes): # tem q receber Alimento.descricao e Alimento.nutrientes
        
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
        if resposta_refeicao.data and len(resposta_refeicao.data) > 0:
            id_refeicao = resposta_refeicao.data[0]['id']

        resposta_alimento = supabase.table('Alimentos').select('id').eq('descricao', descricao).execute()
        if resposta_alimento.data and len(resposta_refeicao.data) > 0:
            id_alimento = resposta_alimento.data[0]['id']

        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()
        if resposta_usuario.data and len(resposta_usuario.data) > 0:
            id_usuario = resposta_usuario.data[0]['id']
        
        dia_refeicao = datetime.today().strftime('%Y-%m-%d')

        response = supabase.table('Historico_Alimentos').insert({
            'dia': dia_refeicao,
            'id_refeicao': id_refeicao,
            'id_alimento': id_alimento,
            'energia' : nutrientes[0],
            'proteina': nutrientes[1],
            'lipideo': nutrientes[2],
            'carboidrato': nutrientes[3],
            'fibra': nutrientes[4],
            'id_usuario': id_usuario
        }).execute()

        if not response.data:  
            print("Nenhum dado encontrado para o alimento selecionado.")
            return False

        if 'error' in response:  
            print("Erro ao buscar dados:", response['error'])
            return False

        print("Alimento salvo com sucesso.")
        return True

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
        
        if not response.data:
            print("Nenhum dado encontrado no histórico.")
            return []

        print("Dados retornados pelo banco:", response.data)
        return response.data
