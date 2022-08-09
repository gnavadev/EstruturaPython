# %%
import numpy as np


class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Armazena onde esta o ultimo elemento do vetor
        # Isso acontece porque por mais que um array tenha 8 elementos, os indices vão de 0 a 7, entao o ultimo indice do array
        # seria o tamanho do array -1 ou no caso , 8 - 1 = 7.
        self.valores = np.empty(self.capacidade, dtype=int)
        # Cria um vetor sem valor algum do tamanho de self.capacidade
        # E com dados do tipo inteiro.

    def imprime(self):
        '''
        se o valor da ultima posicao for -1, significa que o 
        vetor está vazio, nao possui tamanho, ou seja,
        array.len - 1 = -1
        se nao
        para indice no range de (ultima_posicao + 1)
        imprime o indice e o valor no indice.
        o codigo ira parar assim que imprimir o ultimo valor do array
        a variavel ultima posicao vai estar com o valor certo ja que
        a mesa é inicializada com -1
        '''
        if self.ultima_posicao == -1:
            print('O vetor esta vazio! ')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        '''
        considerando 10 elementos, a ultima posicao estara no indice 9
        se a ultima posicao for igual a capacidade - 1 ou seja 10 - 1
        imprime capacidade maxima
        se nao
        adiciona 1 a ultima posicao
        o valor da ultima posicao vai ser igual ao valor inserido
        '''
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade Maxima Atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        '''
        Para i em numero de posicao de vetores + 1 , se o valor digitado pelo usuario
        For igual ao valor no indice I retorna o numero do indice, se nao , retorna -1

        '''
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    def excluir(self, valor):
        '''
        Posicao recebe o indice do valor pesquisado
        se a posicao nao existir , retorna -1
        se nao
        para i em range(comeco, fim):
        o valor no indice atual é igual o valor do próximo índice.
        decrementa o valor da ultima posicao
        '''
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1


vetor = VetorNaoOrdenado(5)
vetor.insere(2)
vetor.insere(3)
vetor.insere(4)
vetor.insere(8)
vetor.insere(10)

vetor.imprime()
vetor.excluir(3)
vetor.imprime()
# %%
