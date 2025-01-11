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


# alimento1 = Alimento()
# alimento1.adicionaAlimento(200,"Arroz, integral, cozido")
# alimento2 = Alimento()
# alimento2.adicionaAlimento(300,"Bolo, mistura para")
# nutrientes_teste = Nutrientes()
# nutrientes_teste.adicionaNutrientes(alimento1)
# nutrientes_teste.adicionaNutrientes(alimento2)
# nutrientes_teste.mostraTotais()
# print(f" Alimento1: {alimento1.nutrientes}")
# print(f"Alimento 2:{alimento2.nutrientes}")
# nutrientes_teste.mostraTotais()
