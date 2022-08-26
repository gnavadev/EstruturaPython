a = [int(input("Digite os numeros do vetor: ")) for x in range(10)]
auxiliar = 0

for i in range(len(a) - 1):  # para i no tamanho do vetor - 1 , caso nao tenha o menos 1 , dara problema no if porque o algoritmo vai tentar
    # comparar com um indice que nao existe
    # para i no tamanho do vetor - 1 , caso nao tenha o menos 1 , dara problema no if porque o algoritmo vai tentar
    for j in range(len(a) - 1):
        # comparar com um indice que nao existe
        if(a[j] > a[j+1]):  # Se o meu valor de indice 0 for maior que o proximo valor
            auxiliar = a[j]  # a variavel auxiliar recebe o valor do indice 0
            a[j] = a[j+1]  # o indice 0 recebe o valor do indice 1
            a[j+1] = auxiliar
        else:
            a[j] = a[j]

print(a)
