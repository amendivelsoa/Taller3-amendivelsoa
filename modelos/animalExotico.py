from abc import ABC, abstractmethod
from modelos.animal import Animal

class Exotico(Animal, ABC):
    def __init__(self, nombre, peso,paisOrigen,impuesto) -> None:
        super().__init__(nombre,peso)
        self._paisOrigen = paisOrigen
        self._impuesto = impuesto
    
    def paisOrigen(self):
        return self._paisOrigen
    
    @abstractmethod
    def impuesto(self):
        pass
    
    @abstractmethod
    def hacerSonido(self):
        pass
    