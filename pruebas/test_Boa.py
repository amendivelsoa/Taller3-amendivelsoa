import unittest
from modelos.boa_Constructor import Boa

class testboa(unittest.TestCase):
    
    def test_sonido(self):
        boa1 = Boa("santana",10.5,"Mexico",14.8)
        self.assertEqual(boa1.hacerSonido(),"TSSS!")
    
    def test_impuesto(self):
        boa1 = Boa("santana",10.5,"Mexico",14.8)
        self.assertEqual(boa1.impuesto(), 155.4)

    def test_alimentarRatones(self):
        boa1 = Boa("santana",10.5,"Mexico",14.8)
        with self.assertRaises(ValueError):
            boa1.alimentar(11)