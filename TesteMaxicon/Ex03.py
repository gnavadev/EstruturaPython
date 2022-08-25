# Ordenar um vetor de 10 posicoes em ordem crescente


vetor = [int(input("Digite 10 valores: ")) for x in range(10)]
acumulador = 0


def ordenaVetor():
    for i in range(len(vetor) - 1):
        for j in range(len(vetor) - 1):
            if vetor[j] > vetor[j + 1]:
                acumulador = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = acumulador


ordenaVetor()
print(vetor)
