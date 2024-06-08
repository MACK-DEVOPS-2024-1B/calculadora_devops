import unittest
import sys
sys.path.append('/workspaces/calculadora_devops/')

from src.dividir import dividir

class TestDividir(unittest.TestCase):

    def test_dividir_positivos(self):
        resultado = dividir(10, 5)
        self.assertEqual(resultado, 2)

    def test_dividir_negativos(self):
        resultado = dividir(-10, -5)
        self.assertEqual(resultado, 2)

    def test_dividir_misto(self):
        resultado = dividir(10, -5)
        self.assertEqual(resultado, -2)

    def test_dividir_mzero(self):
        resultado = dividir(10, 0)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()