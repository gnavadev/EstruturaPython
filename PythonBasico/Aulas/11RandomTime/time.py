import time as tm

print(tm.time())

antes = tm.time()
lista = []
for i in range(0, 100000):
    lista.append(i)
depois = tm.time()
intervalo = depois - antes
print(f"Tempo: {intervalo} segundos")

print("Finalizando...")
tm.sleep(2)
print("...")
tm.sleep(2)
print("Ate a proxima! ")
