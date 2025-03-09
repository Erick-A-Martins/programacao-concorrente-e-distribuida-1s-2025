import threading
import time

L1 = threading.Lock()
L2 = threading.Lock()


def Tarefa1():
    print("T1: tentando adquirir lock1")
    L1.acquire()
    print("T1: Adquiriu lock1, agoran tentando o lock2")
    time.sleep(1)
    L2.acquire()
    print("L1: lock2 adquirido")
    L2.release()
    L1.release()
    print("T1 finalizada!!!")

def Tarefa2():
    print("T2: tentando adquirir lock2")
    L2.acquire()
    print("T2: Adquiriu lock1, agoran tentando o lock1")
    time.sleep(1)
    L1.acquire()
    print("L2: lock1 adquirido")
    L2.release()
    L1.release()
    print("T2 finalizada!!!")


t1 = threading.Thread(target = Tarefa1)
t2 = threading.Thread(target = Tarefa2)
t1.start()
t2.start()
t1.join()
t2.join()

print("Programa encerrado!")
