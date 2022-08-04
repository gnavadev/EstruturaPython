# Crie uma lista vazia e faça a leitura de dois valores do tipo float,
# colocando cada um dos valores nas primeiras posições da lista
#  (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista).
#  Faça a divisão dos dois valores e trate as seguintes exceções:
# - ValueError: se o usuário digitar um caracter
# - ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
# - IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
# - KeyboardInterrupt: caso o usuário interrompa a execução

from numpy import append

resultado = 0
lista_vazia = []

while True:
    try:
        lista_vazia.append(float(input("Digite o primeiro valor: ")))
        lista_vazia.append(float(input("Digite o segundo valor: ")))
        resultado = lista_vazia[0] / lista_vazia[1]
    except ValueError:
        print(f'Valor Invalido {ValueError}')
    except ZeroDivisionError:
        print(f'Valor Invalido {ZeroDivisionError}')
    except IndexError:
        print(f'Indice Invalido {IndexError}')
    except KeyboardInterrupt:
        print('Usuario interrompeu a execucao')
        break
    else:
        print(lista_vazia)
        print(resultado)
        del lista_vazia[0]
        del lista_vazia[-1]
        print(lista_vazia)
