from Alimento import Alimento

class Nutrientes:
    def __init__(self):
        self.total_energia = 0
        self.total_proteina = 0
        self.total_lipideos = 0
        self.total_carboidratos = 0
        self.total_fibra = 0

    def adicionaNutrientes(self, alimento):

        if alimento.nutrientes is None:
            raise ValueError("O alimento não possui dados de nutrientes.")
        
        self.total_energia += alimento.nutrientes[0]
        self.total_proteina += alimento.nutrientes[1]
        self.total_lipideos += alimento.nutrientes[2]
        self.total_carboidratos += alimento.nutrientes[3]
        self.total_fibra += alimento.nutrientes[4]

    def obter_totais(self):
        return {
            "energia": self.total_energia,
            "proteina": self.total_proteina,
            "lipideos": self.total_lipideos,
            "carboidratos": self.total_carboidratos,
            "fibra": self.total_fibra,
        }

    def mostraTotais(self):

        totais = (f"Energia: {self.total_energia:.2f} kcal\n"
                f"Proteína: {self.total_proteina:.2f} g\n"
                f"Lipídeos: {self.total_lipideos:.2f} g\n"
                f"Carboidratos: {self.total_carboidratos:.2f} g\n"
                f"Fibra: {self.total_fibra:.2f} g")
        
        return print(totais)
    
    def obterLista(self):
        lista = [self.total_energia, self.total_proteina, self.total_lipideos, self.total_carboidratos, self.total_fibra]
        return lista 

