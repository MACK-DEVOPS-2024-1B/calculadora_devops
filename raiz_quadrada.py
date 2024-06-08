def calcular_raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo")
    return numero ** 0.5

# Exemplo de uso
try:
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    raiz_quadrada = calcular_raiz_quadrada(numero)
    print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
except ValueError as e:
    print(f"Erro: {e}")