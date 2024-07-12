from modelos.animalExotico import Exotico

class Boa(Exotico):
    def __init__(self, nombre, peso, paisOrigen, impuesto) -> None:
        super().__init__(nombre, peso, paisOrigen, impuesto)
        self._ratones_comidos = 0
    
    def hacerSonido(self):
        return "TSSS!"
    
    def agregar_raton(self):
        self._ratones_comidos += 1

    def impuesto(self):
        return self._peso * self._impuesto
    
    def alimentar(self,cantRatones):
        if cantRatones == 10:
            raise ValueError("Demasidos Ratones")
        else:
            self._ratones_comidos += cantRatones
            print(f"La boa ha comido {cantRatones} ratones.")