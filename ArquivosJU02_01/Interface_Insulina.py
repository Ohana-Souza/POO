from abc import ABC, abstractmethod 

class InterfaceInsulina(ABC):
    @abstractmethod
    def calculaDosagem(self):
        pass

    @abstractmethod
    def verificaAlarme(self):
        pass 

