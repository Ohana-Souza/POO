from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class Alimento:
    def __init__(self, gramas=0 , descricao='', nutrientes=None):
        self.gramas = gramas 
        self.descricao = descricao
        self.nutrientes = nutrientes

    def adicionaAlimento(self, gramas, id_alimento):
        self.gramas = gramas
        response = supabase.table("Alimentos").select(
        '"descricao", "energia(kcal)", "proteina(g)", "lipideos(g)", "carboidrato(g)", "fibra(g)"').eq("id", id_alimento).execute()
    
        if not response.data:  # If no data was returned
            print("Nenhum dado encontrado para o alimento selecionado.")
            return []

        if 'error' in response:  # Check if an error exists
            print("Erro ao buscar dados:", response['error'])
            return []
    
        if response.data:
            row = response.data[0]
            self.descricao = row.get("descricao")  
            self.nutrientes =  [
                row.get("energia(kcal)")*(gramas/100),
                row.get("proteina(g)")*(gramas/100),
                row.get("lipideos(g)")*(gramas/100),
                row.get("carboidrato(g)")*(gramas/100),
                row.get("fibra(g)")*(gramas/100),
            ]
        else:
            print("Nenhum dado encontrado para o alimento selecionado.")
            return []


    def mostraAlimento(self, id_alimento):
        response = supabase.table("Alimentos").select(
        '"descricao", "energia(kcal)", "proteina(g)", "lipideos(g)", "carboidrato(g)", "fibra(g)"').eq("id", id_alimento).execute()
        
        if not response.data:  # If no data was returned
            print("Nenhum dado encontrado para o alimento selecionado.")
            return []

        if 'error' in response:  # Check if an error exists
            print("Erro ao buscar dados:", response['error'])
            return []

        return response.data


    def mostraTodosAlimentos(self):
        response = supabase.table("Alimentos").select("*").execute()
    
        if response.error:
            print("Erro ao buscar dados:", response.error)
            return []
    
        return response.data
    
    



