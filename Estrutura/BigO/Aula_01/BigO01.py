# Funcao O(n)
import timeit


# Essa funcao eh O(11) pois possui 11 passos


def soma1(n):
    soma = 0  # 1 Passo Atribui a variavel
    for i in range(n + 1):
        soma += i  # Faz o comando 10 vezes (com apenas 1 operacao)
    return soma


print(timeit.timeit("soma1(100)", setup="from __main__ import soma1"))

# Essa funcao eh O(3) pois possui 3 passos


def soma2(n):
    return (n * (n + 1)) / 2  # Passos (multiplicacao,adicao,divisao)


print(timeit.timeit("soma2(100)", setup="from __main__ import soma2"))
