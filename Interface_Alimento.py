from abc import ABC, abstractmethod 

class InterfaceAlimento(ABC):
    @abstractmethod
    def AdicionaAlimento(self):
        pass

    @abstractmethod
    def MostraTodosAlimentos(self):
        pass 

