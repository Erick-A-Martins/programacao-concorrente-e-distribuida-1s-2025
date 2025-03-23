import random
import threading
import time

# Função principal do QuickSort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô

    left_list = []
    right_list = []

    thread1 = threading.Thread(target=lambda: left_list.extend(quicksort(left)))
    thread2 = threading.Thread(target=lambda: right_list.extend(quicksort(right)))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    return quicksort(left) + [pivot] + quicksort(right)

# Função para gerar números aleatórios

def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort

if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios()
    
    print("Primeiros 10 números antes da ordenação:", numeros)

    t0 = time.time()
    numeros_ordenados = quicksort(numeros)
    tf = time.time()
    tempo_total = tf - t0
    print(f"Duração do processo: {tf-t0:.2f} segundos")

    print("Primeiros 10 números após a ordenação:", numeros_ordenados)

