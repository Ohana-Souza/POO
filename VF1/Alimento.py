from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class Alimento:
    def __init__(self, gramas=0 , descricao='', nutrientes=None):
        self.gramas = gramas 
        self.descricao = descricao
        self.nutrientes = nutrientes

    def adicionaAlimento(self, gramas, descricao):
        self.gramas = gramas

        # Consulta ao banco de dados baseada na descrição do alimento
        response = supabase.table("Alimentos").select(
            '"descricao", "energia(kcal)", "proteina(g)", "lipideos(g)", "carboidrato(g)", "fibra(g)"'
        ).eq("descricao", descricao).execute()

        # Verifica se a consulta retornou dados
        if not response.data:  # Nenhum dado encontrado
            print(f"Alimento '{descricao}' não encontrado no banco de dados.")
            self.nutrientes = []
            return

        if "error" in response:  # Verifica se ocorreu algum erro
            print("Erro ao buscar dados do alimento:", response["error"])
            self.nutrientes = []
            return

        # Processa os dados retornados
        row = response.data[0]
        self.descricao = row.get("descricao", "Alimento desconhecido")  # Evita valores nulos
        self.nutrientes = [
            row.get("energia(kcal)", 0) * (gramas / 100),  # Energia calculada com base nos gramas
            row.get("proteina(g)", 0) * (gramas / 100),
            row.get("lipideos(g)", 0) * (gramas / 100),
            row.get("carboidrato(g)", 0) * (gramas / 100),
            row.get("fibra(g)", 0) * (gramas / 100),
        ]
        print(f"Alimento processado: {self.descricao}, Nutrientes: {self.nutrientes}")



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
    
    


