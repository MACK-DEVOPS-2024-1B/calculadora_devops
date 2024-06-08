import unittest
import sys

sys.path.append('/workspaces/calculadora_devops/src')
from raiz_quadrada import calcular_raiz_quadrada

class TestCalculoRaizQuadrada(unittest.TestCase):
    def test_raiz_quadrada_numero_positivo(self):
        self.assertAlmostEqual(calcular_raiz_quadrada(9), 3.0)

    def test_raiz_quadrada_zero(self):
        self.assertAlmostEqual(calcular_raiz_quadrada(0), 0.0)

    def test_raiz_quadrada_numero_negativo(self):
        with self.assertRaises(ValueError):
            calcular_raiz_quadrada(-4)

if __name__ == '__main__':
    unittest.main()