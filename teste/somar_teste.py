import unittest
import sys
sys.path.append('/workspaces/calculadora_devops/')  # Adicione o diretório onde o arquivo somar.py está localizado

from somar import somar

class TestSomar(unittest.TestCase):
    def test_somar(self):
        # Teste com números positivos
        self.assertEqual(somar(5, 3), 8)
        
        # Teste com números negativos
        self.assertEqual(somar(-5, -3), -8)
        
        # Teste com um número positivo e outro negativo
        self.assertEqual(somar(5, -3), 2)
        
        # Teste com zero
        self.assertEqual(somar(0, 0), 0)

if __name__ == '__main__':
    unittest.main()



