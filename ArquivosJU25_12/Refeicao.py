
class Refeicao:
    def __init__(self):
        self.alimentos = {}

    def montaRefeicao(self, alimento):
        if alimento.descricao in self.alimentos:
            print(f"Alimento '{alimento.descricao}' já está na refeição.")
        else:
            self.alimentos[alimento.descricao] = alimento
            print(f"Alimento '{alimento.descricao}' adicionado à refeição.")

    def mostraRefeicao(self):
        if not self.alimentos:
            print("A refeição ainda não possui alimentos.")
        else:
            print("Refeição:")
            for descricao, alimento in self.alimentos.items():
                print(f"- Descrição: {descricao}, Nutrientes: {alimento.nutrientes}")

    def somaNutrientes(self):
        nutrientes_totais = [0, 0, 0, 0, 0]  
        for alimento in self.alimentos.values():
            for i in range(len(nutrientes_totais)):
                nutrientes_totais[i] += alimento.nutrientes[i]

        return nutrientes_totais

