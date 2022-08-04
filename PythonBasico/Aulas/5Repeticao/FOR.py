for numero in range(1, 6):  # Mostra os numero de 1 a 5, mostra todos os de 1 ate 6, (1,2,3,4,5)
    print(numero)
print("-------------------------------------------")
for numero in range(5, 0, -1):  # Mostra os numeros de 5 ate 1, com -1 por vez (step)
    print(numero)
print("-------------------------------------------")

soma = 0
for numero in range(1, 6):
    soma = soma + numero
    print(soma)
print("-------------------------------------------")

palavra = 'sorvete'
for letra in palavra:
    print(letra)
    if letra == 'v':
        print("Achou a letra V")
print("-------------------------------------------")
for i in range(0, 5):
    print('---')
    print(i)
    print('---')
    for j in range(0, 3):
        print(j)
