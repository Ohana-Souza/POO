class Verificadora:
    @staticmethod
    def verificar_inteiro(valor: str, tipo: str = "float") -> bool:
        """
        Verifica se um valor pode ser convertido para um tipo específico (float ou int).
        """
        try:
            if tipo == "float":
                float(valor)  # Tenta converter o valor para float
            elif tipo == "int":
                int(valor)  # Tenta converter o valor para int
            else:
                return False  # Tipo inválido
            return True
        except ValueError:
            return False  # Retorna False se a conversão falhar
