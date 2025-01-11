from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class Alimento:
    def __init__(self, gramas=0 , descricao='', nutrientes=None):
        self.gramas = gramas 
        self.descricao = descricao
        self.nutrientes = nutrientes

    def adicionaAlimento(self, descricao, gramas):
        try:
            self.gramas = gramas
            response = supabase.table("Alimentos").select(
                '"descricao", "energia(kcal)", "proteina(g)", "lipideos(g)", "carboidrato(g)", "fibra(g)"'
            ).eq("descricao", descricao).execute()

            if not response.data:
                raise ValueError("Nenhum dado encontrado para o alimento selecionado.")

            row = response.data[0]
            self.descricao = row.get("descricao")
            self.nutrientes = [
                row.get("energia(kcal)", 0) * (gramas / 100),
                row.get("proteina(g)", 0) * (gramas / 100),
                row.get("lipideos(g)", 0) * (gramas / 100),
                row.get("carboidrato(g)", 0) * (gramas / 100),
                row.get("fibra(g)", 0) * (gramas / 100),
            ]

        except Exception as e:
            print(f"Erro ao adicionar alimento: {e}")
            self.nutrientes = None



    def mostraAlimento(self, descricao_alimento):
        response = supabase.table("Alimentos").select(
        '"descricao", "energia(kcal)", "proteina(g)", "lipideos(g)", "carboidrato(g)", "fibra(g)"').eq("descricao", descricao_alimento).execute()
        
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
    
    


alimento_teste = Alimento()
alimento_teste.adicionaAlimento("Arroz, integral, cozido", 200)

if alimento_teste.nutrientes:
    print(f"Nutrientes do alimento: {alimento_teste.nutrientes}")
else:
    print("Erro ao carregar nutrientes.")
