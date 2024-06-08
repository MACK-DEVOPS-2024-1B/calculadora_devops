import unittest
import sys
sys.path.append('/workspaces/calculadora_devops/')

from src.subtrair import subtrair

class TestSubtrair(unittest.TestCase):

    def test_subtrair_positivos(self):
        resultado = subtrair(10, 5)
        self.assertEqual(resultado, 5)

    def test_subtrair_negativos(self):
        resultado = subtrair(-10, -5)
        self.assertEqual(resultado, -5)

    def test_subtrair_misto(self):
        resultado = subtrair(10, -5)
        self.assertEqual(resultado, 15)

if __name__ == '__main__':
    unittest.main()
