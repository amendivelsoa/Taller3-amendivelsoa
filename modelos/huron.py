from modelos.animalExotico import Exotico

class Huron(Exotico):
    def __init__(self, nombre, peso, paisOrigen, impuesto) -> None:
        super().__init__(nombre, peso, paisOrigen, impuesto)

    def hacerSonido(self):
        return "¡Eek Eek!"
    
    def impuesto(self):
        return self._peso * self._impuesto