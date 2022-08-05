import timeit

# O(n) ou no caso O(100)


def lista1():
    lista = []
    for i in range(100):
        lista += [i]
    return lista


print(timeit.timeit("lista1()", setup="from __main__ import lista1"))


def lista2():
    return range(100)


print(timeit.timeit("lista2()", setup="from __main__ import lista2"))


# verificar se lista2 esta sendo gerada ate 100
# l = lista2()
# for i in l:
#     print(i)
