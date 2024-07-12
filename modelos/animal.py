from modelos.ianimales import Ianimal
from abc import ABC, abstractmethod

class Animal (Ianimal,ABC):
    def __init__(self,nombre,peso) -> None:
        self._nombre = nombre
        self._peso = peso

    def obt_nombre(self):
        return self._nombre
    
    def obt_peso(self):
        return self._peso
    
    @abstractmethod
    def hacerSonido(self):
        pass 

    @abstractmethod
    def impuesto(self):
        pass
