import numpy as np

matriz = np.array([[2, 3, 1],  # Matriz com 2 linhas e 3 colunas
                  [4, 5, 7]])

print(matriz)

print(matriz.shape)  # mostra (linhas,colunas) da matriz
print(matriz[0])  # Retorna a primeira linha
print(matriz[1])  # Retorna a segunda linha

print(matriz[0][0])  # Retorna o elemento da linha 0 coluna 0

print("---------------------")


for i in range(matriz.shape[0]):  # (Linhas,Colulas) nesse for estamos
    # percorrendo o primeiro indice, linhas
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])  # Para cada coluna imprime o elemento ij
