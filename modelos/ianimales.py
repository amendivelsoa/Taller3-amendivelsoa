from abc import ABC, abstractmethod

class Ianimal(ABC):

    @abstractmethod
    def hacerSonido(self):
        pass

    @abstractmethod
    def impuesto(self):
        pass
