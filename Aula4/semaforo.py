import threading

S = threading.Semaphore(3)

def trabalho(ID):
    print(f"Thread {ID} iniciou.")
    with S:
        print(f"Thread {ID} entrou no semáforo")
        threading.Event().wait(1)
        print(f"Thread {ID} saindo do semáforo")

    print(f"Thread {ID} finalizou.")


threads = [threading.Thread(target= trabalho, args = (i, )) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()