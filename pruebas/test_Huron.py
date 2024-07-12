import unittest
from modelos.huron import Huron

class testHuron(unittest.TestCase):
    
    def test_sonido(self):
        huron1 = Huron("meliodas",14.8,"venezuela",5.8)
        self.assertEqual(huron1.hacerSonido(),"¡Eek Eek!")
    
    def test_impuesto(self):
         huron1 = Huron("meliodas",14.8,"venezuela",5.8)
         self.assertEqual(huron1.impuesto(), 85.84)
