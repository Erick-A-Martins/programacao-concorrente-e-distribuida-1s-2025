import time
import random
import threading

def SomaQuadrados(dados, media):
    soma = 0
    for x in dados: soma += (x - media) ** 2
    return soma

def CalcularVarianca(dados):
    N = len(dados)

    soma = 0
    for x in dados: soma += x
    media = soma / N

    meio = N // 2
    esquerda = dados[:meio]
    direita = dados[meio:]

    SQEsquerda = 0
    SQDireita = 0

    def ProcessarEsquerda():
        nonlocal SQEsquerda
        SQEsquerda = SomaQuadrados(esquerda, media)

    def ProcessarDireita():
        nonlocal SQDireita
        SQDireita = SomaQuadrados(direita, media)

    TE = threading.Thread(target=ProcessarEsquerda)
    TD = threading.Thread(target=ProcessarDireita)

    TE.start()
    TD.start()

    TE.join()
    TD.join()

    variancia = (SQEsquerda + SQDireita) / N

    return variancia

# Exemplo de uso
l1 = [2, 4, 6, 8, 10]
l2 = [2, 2, 2, 2, 2]
l3 = [random.randint(1, 100) for _ in range(1000000)]

t0 = time.time()
teste = CalcularVarianca(l3)
tf = time.time()
print(f"{teste}")
print(f"{tf - t0:.6f}")
