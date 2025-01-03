from Interface_Insulina import InterfaceInsulina
from typing import Type

class Calculadora_Insulina(InterfaceInsulina):
    def fazCalculoDosagem(self, insulina: Type[InterfaceInsulina]):
        dosagem = insulina.calculaDosagem()
        print(f"Dosagem calculada para a refeição: {dosagem}")

    def fazVerificacaoAlarme(self, insulina: Type[InterfaceInsulina]):
        alarme = insulina.verificaAlarme
        return alarme 


