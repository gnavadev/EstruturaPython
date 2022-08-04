numero = 0
while numero < 6:
    print(numero)
    numero += 1

print("---------------")
numero = 5
while numero > 0:
    print(numero)
    numero -= 1

print("---------------")
# 1 + 2 + 3 + 4 + 5
soma = 0
numero = 1
while numero < 6:
    soma += numero
    numero += 1
    print(soma)
print("---------------")
numero = -1
while numero < 1 or numero > 10:
    numero = int(input("Digite um numero de 1 a 10: "))
