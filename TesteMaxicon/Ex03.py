# Ordenar um vetor de 10 posicoes em ordem crescente

import numpy as np

# Recebo os valores do vetor de 10 posicoes, 0 a 9
vetorFora = [int(input("Digite os valores do vetor: ")) for x in range(10)]


def bbsort(vetor):  # Defino a funcao com o parametro vetor
    n = len(vetor)  # n sera igual o tamanho do vetor que o parametro receber

    for i in range(n):  # Para i no range de n ou no caso, para i no range 10
        for j in range(0, n - i - 1):
            # Para j no range (0, tamanho do vetor -i(apos terminar o primeiro ciclo/ordenacao, isso ira garantir que o valor que esta na ultima posicao
            # nao ira entrar no proximo loop) - 1(para nao tentar ler um valor que nao existe)))
            if vetor[j] > vetor[j + 1]:  # se a posicao da esquerda for maior que a posicao da direita
                temp = vetor[j]  # uma variavel temp recebe o valor da esquerda
                # o valor da esquerda recebe o valor menor da direita
                vetor[j] = vetor[j + 1]
                # O valor da direita , recebe o valor maior, guardado na variavel temp
                vetor[j + 1] = temp
                # apos percorrer e trocar todo o vetor pela primeira vez, o ultimo valor sera o maior ja que o valor maior sempre eh passado para direita
                # O loop de i eh ativado novamente dessa vez com i = 1
                # J agora vale 1 e vai realizar um loop de 0 ate 10 - 1 -1 ou seja de 0 a 8
                # Depois J vale 2 e vai realizar um loop de 0 ate 10 - 2 -1 ou seja de 0 a 7 e assim em diante
                # Perceba que o valor de J sempre eh o que falta para n - i - 0 ser igual a 9
    print(vetor)  # Print do vetor


bbsort(vetorFora)
