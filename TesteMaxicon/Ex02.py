x = 0
# Printar a sequencia de fibonacci ate o centesimo elemento


y = 1
acumulador = 0
print('0')
for i in range(0, 101):
    acumulador = x + y
    y = x
    x = acumulador
    print(acumulador)
