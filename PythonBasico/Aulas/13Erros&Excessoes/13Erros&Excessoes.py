# NameError : variavel nao identificada
# TypeError: tipos de dados incompatives
# RuntimeError: erro de execucao
# SynstaxError: sintaxe invalida
# ZeroDivisionError: divisao por 0
# IndexError: indice esta fora da colecao

# Tratamento de Erros


# while True:
#     try:
#         n = int(input("Digite um numer inteiro: "))
#     except:
#         print(f"Valor Invalido {ValueError}")
#     else:
#         print(f'Valor Digitado eh {n}')
#         break


while True:
    try:
        p = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Valor Invalido')
    except KeyboardInterrupt:
        print('\nUsuario Interrompeu a Excecucao')
        break
    else:
        print(f"Valor Digitado eh {p}")
        break
