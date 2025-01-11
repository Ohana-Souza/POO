

class Verificadora:
    @staticmethod
    def verificar_inteiro(valor, tipo="float"):
        try:
            if tipo == "float":
                return float(valor)
            elif tipo == "int":
                return int(valor)
        except ValueError:
            raise ValueError("Valor inválido. Insira um número válido.")




