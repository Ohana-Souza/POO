from Interface_Insulina import InterfaceInsulina

class Asparge(InterfaceInsulina):
    def __init__(self, peso, tipo_diabetes, dosagem_max, carboidratos, proteinas):
        self.peso = peso
        self.tipo_diabetes = tipo_diabetes
        self.dosagem_max = dosagem_max
        self.carboidratos = carboidratos
        self.proteinas = proteinas

    def calculaDosagem(self):
        """
        Calcula a dose de insulina Aspart (ação rápida) necessária para uma refeição.
        """
        # Estimativa inicial da TDD (Dose Total Diária de insulina)
        if self.tipo_diabetes == "Tipo 1":
            tdd = self.peso * 0.55  # Média de 0,4 a 0,6 UI/kg
        elif self.tipo_diabetes == "Tipo 2":
            tdd = self.peso * 0.3  # Média de 0,2 a 0,5 UI/kg
        elif self.tipo_diabetes == "Pré-diabetes":
            tdd = self.peso * 0.1  # Valores baixos por não ser dependente de insulina
        elif self.tipo_diabetes == "Gestacional":
            tdd = self.peso * 0.6  # Maior necessidade devido à gestação
        
        # Índice de carboidratos (IC) - Quantidade de carboidratos cobertos por 1 unidade de insulina
        ic = 500 / tdd

        # Fator de proteínas convertidas em glicose (10% a 20% da proteína vira glicose)
        glicose_proteina = self.proteinas * 0.15  # Considera 15% da proteína convertida em glicose

        # Total de carboidratos a serem cobertos (incluindo conversão de proteínas)
        carboidratos_totais = self.carboidratos + glicose_proteina

        # Dose de insulina para carboidratos
        dose_insulina = carboidratos_totais / ic

        return round(dose_insulina, 2)  # Retorna o valor arredondado para 2 casas decimais



    def verificaAlarme(self, dose_calculada):
        super().verificaAlarme(dose_calculada, self.dosagem_max)


class Humalog(InterfaceInsulina):
    def __init__(self, peso, tipo_diabetes, dosagem_max, carboidratos, proteinas):
        self.peso = peso
        self.tipo_diabetes = tipo_diabetes
        self.dosagem_max = dosagem_max
        self.carboidratos = carboidratos
        self.proteinas = proteinas

    def calculaDosagem(self):
        """
        Calcula a dose de insulina Humalog (lispro) necessária para uma refeição.
        """
        # Estimativa inicial da TDD (Dose Total Diária de insulina)
        if self.tipo_diabetes == "Tipo 1":
            tdd = self.peso * 0.6  # Média de 0,5 a 0,7 UI/kg para Humalog
        elif self.tipo_diabetes == "Tipo 2":
            tdd = self.peso * 0.35  # Média de 0,3 a 0,6 UI/kg para Humalog
        elif self.tipo_diabetes == "Pré-diabetes":
            tdd = self.peso * 0.12  # Valores baixos por não ser dependente de insulina
        elif self.tipo_diabetes == "Gestacional":
            tdd = self.peso * 0.65  # Maior necessidade devido à gestação
        
        # Índice de carboidratos (IC) - Quantidade de carboidratos cobertos por 1 unidade de insulina
        ic = 500 / tdd

        # Conversão de proteínas em glicose (10% a 20% das proteínas viram glicose)
        glicose_proteina = self.proteinas * 0.15  # Considera 15% da proteína convertida em glicose

        # Total de carboidratos a serem cobertos (incluindo conversão de proteínas)
        carboidratos_totais = self.carboidratos + glicose_proteina

        # Dose de insulina para carboidratos
        dose_insulina = carboidratos_totais / ic

        return round(dose_insulina, 2)  # Retorna o valor arredondado para 2 casas decimais
    

    def verificaAlarme(self, dose_calculada):
        super().verificaAlarme(dose_calculada, self.dosagem_max)
     
        
class NPH(InterfaceInsulina):
    def __init__(self, peso, tipo_diabetes, dosagem_max, carboidratos, proteinas):
        self.peso = peso
        self.tipo_diabetes = tipo_diabetes
        self.dosagem_max = dosagem_max
        self.carboidratos = carboidratos
        self.proteinas = proteinas

    def calculaDosagem(self):
        """
        Calcula a dose de insulina NPH (ação intermediária) necessária para uma refeição.
        """
        # Estimativa inicial da TDD (Dose Total Diária de insulina)
        if self.tipo_diabetes == "Tipo 1":
            tdd = self.peso * 0.45  # Média de 0,4 a 0,5 UI/kg para NPH
        elif self.tipo_diabetes == "Tipo 2":
            tdd = self.peso * 0.25  # Média de 0,2 a 0,3 UI/kg para NPH
        elif self.tipo_diabetes == "Pré-diabetes":
            tdd = self.peso * 0.1  # Valores baixos por não ser dependente de insulina
        elif self.tipo_diabetes == "Gestacional":
            tdd = self.peso * 0.5  # Maior necessidade devido à gestação
        
        ic = 500 / tdd

        glicose_proteina = self.proteinas * 0.15  

        carboidratos_totais = self.carboidratos + glicose_proteina

        dose_insulina = carboidratos_totais / ic

        return round(dose_insulina, 2)  

    def verificaAlarme(self, dose_calculada):
        super().verificaAlarme(dose_calculada, self.dosagem_max)


class Glargina(InterfaceInsulina):
    def __init__(self, peso, tipo_diabetes, dosagem_max, carboidratos, proteinas):
        self.peso = peso
        self.tipo_diabetes = tipo_diabetes
        self.dosagem_max = dosagem_max
        self.carboidratos = carboidratos
        self.proteinas = proteinas

    def calculaDosagem(self):
        """
        Calcula a dose de insulina Glargina (ação prolongada) necessária para uma refeição.
        """
        # Estimativa inicial da TDD (Dose Total Diária de insulina)
        if self.tipo_diabetes == "Tipo 1":
            tdd = self.peso * 0.5  # Média de 0,4 a 0,6 UI/kg para Glargina
        elif self.tipo_diabetes == "Tipo 2":
            tdd = self.peso * 0.3  # Média de 0,2 a 0,4 UI/kg para Glargina
        elif self.tipo_diabetes == "Pré-diabetes":
            tdd = self.peso * 0.12  # Valores baixos por não ser dependente de insulina
        elif self.tipo_diabetes == "Gestacional":
            tdd = self.peso * 0.55  # Necessidade maior devido à gestação
        

        ic = 500 / tdd

        glicose_proteina = self.proteinas * 0.15  

        carboidratos_totais = self.carboidratos + glicose_proteina

        dose_insulina = carboidratos_totais / ic


        return round(dose_insulina, 2)  

    def verificaAlarme(self, dose_calculada):
        super().verificaAlarme(dose_calculada, self.dosagem_max)



from Usuario import Usuario
from Perfil_Medico import PerfilMedico
from Alimento import Alimento
from Calculadora_Insulina import Calculadora_Insulina
from Nutrientes import Nutrientes
from Interface_Insulina import InterfaceInsulina

Usuario_teste = Usuario("juliateste@gmail.com")
Usuario_teste.autenticacao_usuario("senha")
Perfil_teste = PerfilMedico(Usuario_teste.email,"Feminino",153,43,19,"Leve","Tipo 1","Sim","Asperge",15)
alimento1 = Alimento()
alimento1.adicionaAlimento(200,"Arroz, integral, cozido")
alimento2 = Alimento()
alimento2.adicionaAlimento(500,"Bolo, mistura para")
nutrientes_teste = Nutrientes()
nutrientes_teste.adicionaNutrientes(alimento1)
nutrientes_teste.adicionaNutrientes(alimento2)
nutrientes_teste.mostraTotais()
insulina_teste = Humalog(Perfil_teste.peso, Perfil_teste.tipo_diabetes, nutrientes_teste.total_carboidratos,nutrientes_teste.total_proteina, Perfil_teste.dosagem_max)
calculadora = Calculadora_Insulina() 
dose_calculada = calculadora.fazCalculoDosagem(insulina_teste)
print(dose_calculada)
alarme = calculadora.fazVerificacaoAlarme(insulina_teste, dose_calculada)

