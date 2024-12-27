from Interface_Insulina import InterfaceInsulina
from typing import Type

class Analise(InterfaceInsulina):
    def fazCalculoDosagem(self, insulina: Type[InterfaceInsulina]):
        pass

    def fazMostraDosagem(self, insulina: Type[InterfaceInsulina]):
        pass
