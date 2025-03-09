import threading
import time

def Tarefa():
    print("Início...")
    time.sleep(3)
    print("Fim...")

T = threading.Thread(target = Tarefa)
T.start()
# T.join()
print("Thread principal finalizada")