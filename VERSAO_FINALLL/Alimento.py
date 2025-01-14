from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY
from typing import List, Optional, Any

# Inicializa o cliente Supabase para comunicação com o banco de dados
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class Alimento:
    def __init__(self, gramas: float = 0, descricao: str = '', nutrientes: Optional[List[float]] = None) -> None:

        self.gramas: float = gramas
        self.descricao: str = descricao
        self.nutrientes: Optional[List[float]] = nutrientes

    def adicionaAlimento(self, gramas: float, descricao: str) -> Optional[List[float]]:

        self.gramas = gramas
        # Busca os dados do alimento no banco de dados
        response = supabase.table("Alimentos").select(
            '"descricao", "energia(kcal)", "proteina(g)", "lipideos(g)", "carboidrato(g)", "fibra(g)"'
        ).eq("descricao", descricao).execute()

        # Verifica se os dados foram encontrados
        if not response.data:
            print("Nenhum dado encontrado para o alimento selecionado.")
            return None

        # Calcula os nutrientes com base na quantidade informada
        row = response.data[0]
        self.descricao = row.get("descricao")
        self.nutrientes = [
            row.get("energia(kcal)") * (gramas / 100),
            row.get("proteina(g)") * (gramas / 100),
            row.get("lipideos(g)") * (gramas / 100),
            row.get("carboidrato(g)") * (gramas / 100),
            row.get("fibra(g)") * (gramas / 100),
        ]
        return self.nutrientes

    def mostraAlimento(self, descricao_alimento: str) -> Optional[List[Any]]:
        """
        Recupera os dados nutricionais completos de um alimento específico do banco de dados.

        Args:
            descricao_alimento (str): Nome ou descrição do alimento a ser buscado.

        Returns:
            Optional[List[Any]]: Dados nutricionais do alimento selecionado.
        """
        response = supabase.table("Alimentos").select(
            '"descricao", "energia(kcal)", "proteina(g)", "lipideos(g)", "carboidrato(g)", "fibra(g)"'
        ).eq("descricao", descricao_alimento).execute()

        # Verifica se os dados foram encontrados no banco
        if not response.data:
            print("Nenhum dado encontrado para o alimento selecionado.")
            return None

        return response.data

    def mostraTodosAlimentos(self) -> List[Any]:
        """
        Retorna todos os alimentos cadastrados no banco de dados com seus respectivos valores nutricionais.
        """
        response = supabase.table("Alimentos").select("*").execute()

        # Verifica se houve erro na consulta
        if response.error:
            print("Erro ao buscar dados:", response.error)
            return []

        return response.data
