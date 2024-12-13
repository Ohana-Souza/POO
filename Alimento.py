from Interface_Alimento import InterfaceAlimento
from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class Alimento(InterfaceAlimentos):
    def __init__(self, gramas=0 , descricao='', nutrientes=None):
        self.gramas = gramas 
        self.descricao = descricao
        self.nutrientes = nutrientes

    def adicionaAlimento(self, id_alimento):
        response = supabase.table("Alimentos").select(
        "descricao, energia(kcal), proteina(g), lipideos(g), carboidrato(g), fibra(g)").eq("id", id_alimento).execute()
    
        if response.error:
            print("Erro ao buscar dados:", response.error)
            return []
    
        if response.data:
            row = response.data[0]
            self.descricao = row.get("descricao")  
            self.nutrientes =  [
                row.get("energia(kcal)"),
                row.get("proteina(g)"),
                row.get("lipideos(g)"),
                row.get("carboidrato(g)"),
                row.get("fibra(g)"),
            ]
        else:
            print("Nenhum dado encontrado para o alimento selecionado.")
            return []


    def mostraAlimento(self, id_alimento):
        response = supabase.table(Alimentos).select(
        "descricao, energia(kcal), proteina(g), lipideos(g), carboidrato(g), fibra(g)").eq("id", id_alimento).execute()
        
        if response.error:
            print("Erro ao buscar dados:", response.error)
            return []

        return response.data


    def mostraTodosAlimentos(self):
        response = supabase.table("Alimentos").select("*").execute()
    
        if response.error:
            print("Erro ao buscar dados:", response.error)
            return []
    
        return response.data



