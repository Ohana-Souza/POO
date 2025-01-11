class Verificadora:
    @staticmethod
    def verificar_inteiro(valor, tipo="float"):
        try:
            if tipo == "float":
                float(valor)
            elif tipo == "int":
                int(valor)
            return True
        except ValueError:
            return False
