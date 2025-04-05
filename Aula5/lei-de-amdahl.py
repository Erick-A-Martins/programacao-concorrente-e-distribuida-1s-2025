import matplotlib.pyplot as plt

def amdahl(f, p_values):
    result = [(p, 1/((1 - f) + f/p)) for p in p_values]
    return result

f = 0.6
p_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50, 60]

speedups = amdahl(f, p_values)

for p, speedup in speedups:
    print(f"{p}\t{speedup:.3f}")


plt.plot(p_values, [s[1] for s in speedups], marker = 'o')
plt.xlabel("Número de processadores")
plt.ylabel("SpeedUp")
plt.title(f"Speedup vs processadores para f = {f}")
plt.grid()
plt.show()