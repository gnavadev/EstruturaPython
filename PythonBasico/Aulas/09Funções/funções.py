
# def mensagem():
#     print("Texto da função")
# mensagem()

from tkinter import E


def mensagem(texto):
    print(texto)


mensagem('Texto1')


# def soma(a, b):
#     print(a + b)


# soma(4, 5)


# def soma(a, b):
#     return a+b


# print(soma(5, 3))

def calcula_energia_potencial_gravitacional(m, h, g=10):
    '''
    Calcula a energia potencial gravitacional
    '''
    e = g * m * h
    return e


print(calcula_energia_potencial_gravitacional(30, 12))
help(calcula_energia_potencial_gravitacional)
