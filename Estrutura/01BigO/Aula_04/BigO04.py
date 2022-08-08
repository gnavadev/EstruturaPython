# %%

# Funcao constante


lista = [1, 2, 3, 4, 5]


def constant(n):
    print(n[0])


    # Por maior que seja a lista, a funcao
    # sempre vai retornar apenas 1 valor
constant(lista)
# %%

# Funcao linear


def linear(n):
    for i in n:
        print(i)

# Vai sempre depender do valor de N


linear(lista)

# %%

#Quadratica - O(n^2) - Polynomial


def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('----')


# Essa funcao vai percorrer o primeiro elemento do array
# No caso [1] e depois vai percorrer todo array [1,2,3,4,5]
# Ate chegar em [5] [1,2,3,4,5]
quadratic(lista)

# %%

# Combinacao

#O(1) + O(5) + O(n) + O(n) + O(3)
# OU
# O(9) + O(2n) -> Mesma coisa que O(n) porque n eh considerado infinito


def combination(n):
    # O(1)
    print(n[0])

    # O(5)
    for i in range(5):
        print('test ', i)

    # O(n)
    for i in n:
        print(i)

    # O(n)
    for i in n:
        print(i)

    # O(3)
    print('Python')
    print('Python')
    print('Python')


combination(lista)
