class Calculadora_Nutrientes:
    def __init__(self, peso: float, altura: float, sexo: str, atividade_fisica: str, tipo_diabetes: str):
        """
        Inicializa a calculadora com os dados do usuário.
        """
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.atividade_fisica = atividade_fisica
        self.tipo_diabetes = tipo_diabetes

    def calcula_tmb(self) -> float:
        """
        Calcula a Taxa Metabólica Basal (TMB) usando a fórmula de Harris-Benedict,
        levando em consideração o sexo do usuário.
        """
        if self.sexo == "Masculino":
            return 10 * self.peso + 6.25 * self.altura - 5 * 30 + 5  # Idade padrão: 30 anos
        elif self.sexo == "Feminino":
            return 10 * self.peso + 6.25 * self.altura - 5 * 30 - 161  # Idade padrão: 30 anos
        else:
            raise ValueError("Sexo inválido. Escolha entre 'Masculino' ou 'Feminino'.")

    def calcula_gcd(self) -> float:
        """
        Calcula o Gasto Calórico Diário (GCD) com base na TMB e no nível de atividade física.
        """
        tmb = self.calcula_tmb()  # Chama o cálculo da TMB
        fator_atividade = {
            "Baixo": 1.2,   # Sedentário
            "Médio": 1.55,  # Atividade moderada
            "Alto": 1.9     # Atividade intensa
        }
        if self.atividade_fisica not in fator_atividade:
            raise ValueError("Nível de atividade física inválido.")
        return tmb * fator_atividade[self.atividade_fisica]

    def calcula_macros(self) -> dict:
        """
        Calcula a distribuição ideal de macronutrientes (carboidratos, proteínas, lipídios e fibras)
        com base no GCD e no tipo de diabetes do usuário.
        """
        gcd = self.calcula_gcd()  # Obtém o gasto calórico diário

        # Define os percentuais de macronutrientes conforme o tipo de diabetes
        if self.tipo_diabetes in ["Tipo 1", "Tipo 2", "Gestacional"]:
            carb_percent = 0.45  # Carboidratos reduzidos
            prot_percent = 0.25  # Proteínas
            lip_percent = 0.30  # Lipídios
        elif self.tipo_diabetes == "Pré-diabetes":
            carb_percent = 0.50  # Carboidratos moderados
            prot_percent = 0.20  # Proteínas
            lip_percent = 0.30  # Lipídios
        else:
            raise ValueError("Tipo de diabetes inválido.")

        # Converte os percentuais de macronutrientes para gramas
        carb_gramas = (gcd * carb_percent) / 4  # 1 g de carboidrato = 4 kcal
        prot_gramas = (gcd * prot_percent) / 4  # 1 g de proteína = 4 kcal
        lip_gramas = (gcd * lip_percent) / 9  # 1 g de lipídio = 9 kcal

        # Calcula a quantidade de fibras (14 g por 1000 kcal)
        fibras_gramas = (gcd / 1000) * 14

        # Retorna os valores arredondados para facilitar a leitura
        return {
            "Carboidratos (g)": round(carb_gramas, 2),
            "Proteínas (g)": round(prot_gramas, 2),
            "Lipídeos (g)": round(lip_gramas, 2),
            "Fibras (g)": round(fibras_gramas, 2),
        }
