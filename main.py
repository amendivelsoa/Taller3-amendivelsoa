from modelos.animal import Animal
from modelos.boa_Constructor import Boa
from modelos.huron import Huron

boa1 = Boa("santana",10.5,"Mexico",14.8)
huron1 = Huron("meliodas",14.8,"venezuela",5.8)

print("-----------------------------------------------------------------")
print("INFORMACION SERPIENTE.")
print("-----------------------------------------------------------------")
print("nombre de la Serpiente: ", boa1.obt_nombre())
print("Sonido de serpiente: ", boa1.hacerSonido())
print("Costo de Importacion: ", boa1.impuesto())
boa1.agregar_raton()
boa1.agregar_raton()
print("ratones ",boa1._ratones_comidos)
print("-----------------------------------------------------------------")
print("INFORMACION HURON.")
print("-----------------------------------------------------------------")
print("nombre del huron: ", huron1.obt_nombre())
print("Sonido del huron: ", huron1.hacerSonido())
print("Costo de Importacion: ", huron1.impuesto())
print("-----------------------------------------------------------------")