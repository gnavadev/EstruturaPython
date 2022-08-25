print("Atribua valores ao vetor 1: ")
vetor1 = [int(input("Digite um numero: ")) for x in range(5)]
nPares = 0
nImpares = 0
nMc = 0
nMs = 0

for y in range(len(vetor1)):
    if vetor1[y] % 2 == 0 or vetor1[y] == 0:
        nPares = nPares + 1
    elif vetor1[y] % 2 != 0:
        nImpares = nImpares + 1
    if vetor1[y] > 50:
        nMc = nMc + 1
    elif vetor1[y] < 7:
        nMs = nMs + 1


print(f"{nPares} numeros pares || {nImpares} numeros impares || {nMc} numeros maiores que 50 || {nMs} numeros menores que 7")
