import sys
import os

# Adiciona o diretório 'src' ao sys.path para que os testes possam importar módulos de 'src'.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from multiplicar import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicacao_positiva(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_multiplicacao_negativa(self):
        self.assertEqual(multiplicar(-3, 4), -12)

    def test_multiplicacao_zero(self):
        self.assertEqual(multiplicar(5, 0), 0)

if __name__ == '__main__':
    unittest.main()
