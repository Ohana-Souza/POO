
class Calculadora_Nutrientes:
    def __init__(self, peso, altura, sexo, atividade_fisica, tipo_diabetes):
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.atividade_fisica = atividade_fisica
        self.tipo_diabetes = tipo_diabetes
    
    def calcula_tmb(self):
        """
        Calcula a Taxa Metabólica Basal (TMB) usando a fórmula de Harris-Benedict.
        """
        if self.sexo == "Masculino":
            return 10 * self.peso + 6.25 * self.altura - 5 * 30 + 5  # Exemplo: idade padrão de 30 anos
        elif self.sexo == "Feminino":
            return 10 * self.peso + 6.25 * self.altura - 5 * 30 - 161  # Exemplo: idade padrão de 30 anos
    
    def calcula_gcd(self):
        """
        Calcula o Gasto Calórico Diário (GCD) com base na TMB e no nível de atividade física.
        """
        tmb = self.calcular_tmb()
        fator_atividade = {"Baixo": 1.2, "Médio": 1.55, "Alto": 1.9}
        return tmb * fator_atividade[self.atividade_fisica]
    
    def calcula_macros(self):
        """
        Calcula a quantidade ideal de carboidratos, proteínas, lipídeos e fibras diárias em gramas.
        
        Retorno:
        - Um dicionário com as quantidades ideais em gramas.
        """
        gcd = self.calcular_gcd()
        
        # Percentuais de macronutrientes (padrão, ajustado para diabetes):
        if self.tipo_diabetes in ["Tipo 1", "Tipo 2", "Gestacional"]:
            carb_percent = 0.45  # Reduzido
            prot_percent = 0.25
            lip_percent = 0.30
        elif self.tipo_diabetes == "Pré-diabetes":
            carb_percent = 0.50  # Moderado
            prot_percent = 0.20
            lip_percent = 0.30
        else:
            raise ValueError("Tipo de diabetes inválido.")
        
        # Cálculo dos macronutrientes
        carb_gramas = (gcd * carb_percent) / 4  # 1 g de carboidrato = 4 kcal
        prot_gramas = (gcd * prot_percent) / 4  # 1 g de proteína = 4 kcal
        lip_gramas = (gcd * lip_percent) / 9  # 1 g de lipídio = 9 kcal

        # Fibras (recomendação: 14 g por 1000 kcal consumidas)
        fibras_gramas = (gcd / 1000) * 14

        return {
            "Carboidratos (g)": round(carb_gramas, 2),
            "Proteínas (g)": round(prot_gramas, 2),
            "Lipídeos (g)": round(lip_gramas, 2),
            "Fibras (g)": round(fibras_gramas, 2),
        }


