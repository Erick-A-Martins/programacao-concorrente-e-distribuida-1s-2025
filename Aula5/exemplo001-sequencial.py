import time
import random

def CalcularVarianca(dados):
    N = len(dados)

    soma = 0
    for x in dados: soma += x
    media = soma / N

    somaDQ = 0
    for x in dados: somaDQ += (x - media) ** 2
    variancia = somaDQ / N

    return variancia

# Exemplo de uso
l1 = [2, 4, 6, 8, 10]
l2 = [2, 2, 2, 2, 2]
l3 = [random.randint(1, 100) for _ in range(1000000)]

t0 = time.time()
teste1 = CalcularVarianca(l3)
tf = time.time()
print(f"{teste1}")
print(f"{tf - t0:.6f}")
