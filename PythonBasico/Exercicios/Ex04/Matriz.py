<<<<<<< HEAD
# Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
# matriz = np.array([[3, 4, 1],
#                    [3, 1, 5]])

import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
acumulador = 0

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        acumulador = acumulador + matriz[i][j]
        print(matriz[i][j])
print(acumulador)
=======
# Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
# matriz = np.array([[3, 4, 1],
#                    [3, 1, 5]])

import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
acumulador = 0

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        acumulador = acumulador + matriz[i][j]
        print(matriz[i][j])
print(acumulador)
>>>>>>> e0de5cb675f7fef4e79db06ff7280c575441d54a
