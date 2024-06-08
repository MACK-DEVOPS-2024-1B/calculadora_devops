def somar_numeros(numero1, numero2):
    soma = numero1 + numero2
    return soma

# Exemplo de uso da função
resultado = somar_numeros(5, 3)
print("O resultado da soma é:", resultado)

import unittest

def somar_numeros(numero1, numero2):
    soma = numero1 + numero2
    return soma

class TestSomarNumeros(unittest.TestCase):
    def test_somar_numeros(self):
        # Teste com números positivos
        self.assertEqual(somar_numeros(5, 3), 8)
        
        # Teste com números negativos
        self.assertEqual(somar_numeros(-5, -3), -8)
        
        # Teste com um número positivo e outro negativo
        self.assertEqual(somar_numeros(5, -3), 2)
        
        # Teste com zero
        self.assertEqual(somar_numeros(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

