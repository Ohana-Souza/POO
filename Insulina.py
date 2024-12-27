from Interface_Insulina import InterfaceInsulina


class Asparge(InterfaceInsulina):

    def calculaDosagem(peso, tipo_diabetes, dosagem_max, carboidratos, proteinas):
        """
        Calcula a dose de insulina Aspart (ação rápida) necessária para uma refeição.
        """
        # Estimativa inicial da TDD (Dose Total Diária de insulina)
        if tipo_diabetes == "Tipo 1":
            tdd = peso * 0.55  # Média de 0,4 a 0,6 UI/kg
        elif tipo_diabetes == "Tipo 2":
            tdd = peso * 0.3  # Média de 0,2 a 0,5 UI/kg
        elif tipo_diabetes == "Pré-diabetes":
            tdd = peso * 0.1  # Valores baixos por não ser dependente de insulina
        elif tipo_diabetes == "Gestacional":
            tdd = peso * 0.6  # Maior necessidade devido à gestação
        
        # Índice de carboidratos (IC) - Quantidade de carboidratos cobertos por 1 unidade de insulina
        ic = 500 / tdd

        # Fator de proteínas convertidas em glicose (10% a 20% da proteína vira glicose)
        glicose_proteina = proteinas * 0.15  # Considera 15% da proteína convertida em glicose

        # Total de carboidratos a serem cobertos (incluindo conversão de proteínas)
        carboidratos_totais = carboidratos + glicose_proteina

        # Dose de insulina para carboidratos
        dose_insulina = carboidratos_totais / ic

        dose_insulina_final = min(dose_insulina, dosagem_max)

        return round(dose_insulina_final, 2)  # Retorna o valor arredondado para 2 casas decimais



    def verificaAlarme(dose_calculada, dosagem_maxima):
    
        if dose_calculada > dosagem_maxima:
            print("\n⚠️ ALARME: A dose calculada excede a dose máxima do perfil médico!")
            print(f"Dose calculada: {dose_calculada} unidades")
            print(f"Dose máxima permitida: {dosagem_maxima} unidades")
            print("Consulte seu médico ou profissional de saúde antes de administrar essa dose.\n")
        else:
            print("\n✅ A dose calculada está dentro dos limites seguros.\n")


class Humalog(InterfaceInsulina):
    def calculaDosagem(peso, tipo_diabetes, carboidratos, proteinas, dosagem_max):
        """
        Calcula a dose de insulina Humalog (lispro) necessária para uma refeição.
        """
        # Estimativa inicial da TDD (Dose Total Diária de insulina)
        if tipo_diabetes == "Tipo 1":
            tdd = peso * 0.6  # Média de 0,5 a 0,7 UI/kg para Humalog
        elif tipo_diabetes == "Tipo 2":
            tdd = peso * 0.35  # Média de 0,3 a 0,6 UI/kg para Humalog
        elif tipo_diabetes == "Pré-diabetes":
            tdd = peso * 0.12  # Valores baixos por não ser dependente de insulina
        elif tipo_diabetes == "Gestacional":
            tdd = peso * 0.65  # Maior necessidade devido à gestação
        
        # Índice de carboidratos (IC) - Quantidade de carboidratos cobertos por 1 unidade de insulina
        ic = 500 / tdd

        # Conversão de proteínas em glicose (10% a 20% das proteínas viram glicose)
        glicose_proteina = proteinas * 0.15  # Considera 15% da proteína convertida em glicose

        # Total de carboidratos a serem cobertos (incluindo conversão de proteínas)
        carboidratos_totais = carboidratos + glicose_proteina

        # Dose de insulina para carboidratos
        dose_insulina = carboidratos_totais / ic

        dose_insulina_final = min(dose_insulina, dosagem_max)

        return round(dose_insulina_final, 2)  # Retorna o valor arredondado para 2 casas decimais



    def verificaAlarme(dose_calculada, dosagem_maxima):
    
        if dose_calculada > dosagem_maxima:
            print("\n⚠️ ALARME: A dose calculada excede a dose máxima do perfil médico!")
            print(f"Dose calculada: {dose_calculada} unidades")
            print(f"Dose máxima permitida: {dosagem_maxima} unidades")
            print("Consulte seu médico ou profissional de saúde antes de administrar essa dose.\n")
        else:
            print("\n✅ A dose calculada está dentro dos limites seguros.\n")
     
        

