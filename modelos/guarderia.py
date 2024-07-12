from modelos.huron import Huron
from modelos.boa_Constructor import Boa

class Guarderia:

    def __init__(self) -> None:
        self.boa1 = Boa("santana",10.5,"Mexico",14.8)
        self.boa2 = Boa("meredi",8.5,"Venezuela",15.8)
        self.huron1 = Huron("meliodas",14.8,"venezuela",5.8)
        self.huron2 = Huron("Karens",55.8,"Colombia",54.8)
    
    def alimentarBoa(self,boa):
        try:
            if boa is None:
                raise ValueError("Esta boa ya es existente!")
            boa.alimentar(5)
        except ValueError as e:
            print(e)