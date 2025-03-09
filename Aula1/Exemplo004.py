import threading
import time

def Saudacao(nome, tempo):
    print(f"Olá, {nome}!")
    time.sleep(tempo)
    print(f"Tchau, {nome}.")

TA = threading.Thread(target = Saudacao, args = ("Ana", 5))
TB = threading.Thread(target = Saudacao, args = ("Beatriz", 2))

t0 = time.time()
TA.start()
TA.join()
TB.start()
TB.join()
tf = time.time()

print(f"Tempo de processamento: {tf-t0} segundos")
print("Fim da execução do código-fonte")