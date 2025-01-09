from Interface_Insulina import InterfaceInsulina
from typing import Type

class Calculadora_Insulina:

    def fazCalculoDosagem(self, insulina: Type[InterfaceInsulina]):
        dosagem = insulina.calculaDosagem()
        print(f"Dosagem calculada para a refeição: {dosagem}")
        return dosagem

    def fazVerificacaoAlarme(self, insulina: Type[InterfaceInsulina], dosagem_calculada):
        alarme = insulina.verificaAlarme(dosagem_calculada)
        return alarme 


