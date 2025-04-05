import time 
import threading

def tarefa(id):
    print(f"Tarefa {id} iniciada.")
    time.sleep(2)
    print(f"Tarefa {id} concluida.")

def main_sequencial():
    t0 = time.time()
    for i in range(4): tarefa(i)
    tf = time.time()
    return tf - t0

def main_paralela():
    t0 = time.time()
    threads = []
    for i in range(4):
        thread = threading.Thread(target=tarefa, args = (i,))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
    tf = time.time()
    return tf - t0

# Versão sequencial
t_seq = main_sequencial()

t_par = main_paralela()
print(f"Sequencial: {t_par}")

speedup = t_seq / t_par