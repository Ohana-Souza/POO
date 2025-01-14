class Refeicao:
    def __init__(self) -> None:
        """
        Inicializa uma refeição vazia com um dicionário de alimentos.
        """
        self.alimentos = {}  # Dicionário que armazena os alimentos na refeição

    def montaRefeicao(self, alimento:str) -> None:
        """
        Adiciona um alimento à refeição. Verifica se o alimento já está na refeição.
        """
        if alimento.descricao in self.alimentos:
            print(f"Alimento '{alimento.descricao}' já está na refeição.")
        else:
            self.alimentos[alimento.descricao] = alimento
            print(f"Alimento '{alimento.descricao}' adicionado à refeição.")

    def mostraRefeicao(self) -> None:
        """
        Mostra os alimentos adicionados à refeição e seus nutrientes.
        """
        if not self.alimentos:
            print("A refeição ainda não possui alimentos.")
        else:
            print("Refeição:")
            for descricao, alimento in self.alimentos.items():
                print(f"- Descrição: {descricao}, Nutrientes: {alimento.nutrientes}")

    def somaNutrientes(self) -> list:
        """
        Calcula e retorna a soma dos nutrientes de todos os alimentos na refeição.
        """
        nutrientes_totais = [0, 0, 0, 0, 0]  # Inicializa a lista de nutrientes totais
        for alimento in self.alimentos.values():
            for i in range(len(nutrientes_totais)):
                nutrientes_totais[i] += alimento.nutrientes[i]

        return nutrientes_totais
