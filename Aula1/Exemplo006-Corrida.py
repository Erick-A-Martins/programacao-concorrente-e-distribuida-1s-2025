import threading
import time

Contador = 0 # Recurso compartilhado
L = threading.Lock()


def Incrementar():
    global Contador
    for _ in range(5000):
        x = Contador
        time.sleep(0.0001)
        x = x + 1
        Contador = x

ListaDeThreads = []

for _ in range(50):
    t = threading.Thread(target = Incrementar)
    ListaDeThreads.append(t)
    t.start()

for t in ListaDeThreads:
    t.join()


print(f"Valor final do Contador: {Contador}")