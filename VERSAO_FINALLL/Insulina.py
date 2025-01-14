from Interface_Insulina import InterfaceInsulina

class Asparge(InterfaceInsulina):
    def __init__(self, peso: float, tipo_diabetes: str, dosagem_max: float, carboidratos: float, proteinas: float) -> None:
        """
        Inicializa a classe Asparge.
        """
        self.peso = peso
        self.tipo_diabetes = tipo_diabetes
        self.dosagem_max = dosagem_max
        self.carboidratos = carboidratos
        self.proteinas = proteinas

    def calculaDosagem(self) -> float:
        """
        Calcula a dose de insulina Aspart necessária para uma refeição.
        """
        # Cálculo da TDD e dose de insulina
        if self.tipo_diabetes == "Tipo 1":
            tdd = self.peso * 0.55
        elif self.tipo_diabetes == "Tipo 2":
            tdd = self.peso * 0.3
        elif self.tipo_diabetes == "Pré-diabetes":
            tdd = self.peso * 0.1
        elif self.tipo_diabetes == "Gestacional":
            tdd = self.peso * 0.6

        ic = 500 / tdd
        glicose_proteina = self.proteinas * 0.15
        carboidratos_totais = self.carboidratos + glicose_proteina
        dose_insulina = carboidratos_totais / ic

        return round(dose_insulina, 2)

    def verificaAlarme(self, dose_calculada: float) -> str:
        """
        Verifica se a dose calculada excede a dosagem máxima permitida.
        """
        return super().verificaAlarme(dose_calculada, self.dosagem_max)


class Humalog(Asparge):
    def calculaDosagem(self) -> float:
        """
        Calcula a dose de insulina Humalog necessária para uma refeição.
        """
        if self.tipo_diabetes == "Tipo 1":
            tdd = self.peso * 0.6
        elif self.tipo_diabetes == "Tipo 2":
            tdd = self.peso * 0.35
        elif self.tipo_diabetes == "Pré-diabetes":
            tdd = self.peso * 0.12
        elif self.tipo_diabetes == "Gestacional":
            tdd = self.peso * 0.65

        ic = 500 / tdd
        glicose_proteina = self.proteinas * 0.15
        carboidratos_totais = self.carboidratos + glicose_proteina
        dose_insulina = carboidratos_totais / ic

        return round(dose_insulina, 2)


class NPH(Asparge):
    def calculaDosagem(self) -> float:
        """
        Calcula a dose de insulina NPH necessária para uma refeição.
        """
        if self.tipo_diabetes == "Tipo 1":
            tdd = self.peso * 0.45
        elif self.tipo_diabetes == "Tipo 2":
            tdd = self.peso * 0.25
        elif self.tipo_diabetes == "Pré-diabetes":
            tdd = self.peso * 0.1
        elif self.tipo_diabetes == "Gestacional":
            tdd = self.peso * 0.5

        ic = 500 / tdd
        glicose_proteina = self.proteinas * 0.15
        carboidratos_totais = self.carboidratos + glicose_proteina
        dose_insulina = carboidratos_totais / ic

        return round(dose_insulina, 2)


class Glargina(Asparge):
    def calculaDosagem(self) -> float:
        """
        Calcula a dose de insulina Glargina necessária para uma refeição.
        """
        if self.tipo_diabetes == "Tipo 1":
            tdd = self.peso * 0.5
        elif self.tipo_diabetes == "Tipo 2":
            tdd = self.peso * 0.3
        elif self.tipo_diabetes == "Pré-diabetes":
            tdd = self.peso * 0.12
        elif self.tipo_diabetes == "Gestacional":
            tdd = self.peso * 0.55

        ic = 500 / tdd
        glicose_proteina = self.proteinas * 0.15
        carboidratos_totais = self.carboidratos + glicose_proteina
        dose_insulina = carboidratos_totais / ic

        return round(dose_insulina, 2)
