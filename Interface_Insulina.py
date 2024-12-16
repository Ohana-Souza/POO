from abc import ABC, abstractmethod 

class InterfaceAlimento(ABC):
    @abstractmethod
    def calculaDosagem(self):
        pass

    @abstractmethod
    def mostraDosagem(self):
        pass 

