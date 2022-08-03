tupla = ('Homo sapiens', 'Canis familiaris', 'Felis Catus')
print(tupla[0])
print(tupla.index('Canis familiaris'))

for elemento in tupla:
    print(elemento)

lista1 = ['Homo sapiens', 'Canis familiaris', 'Felis Catus']
lista2 = ['Xenopus laeves', 'Ailuropoda melanoleuca']

lista3 = lista1 + lista2  # Concatena listas
print(lista3)
lista2_2 = lista2 * 2  # Multiplica a lista
print(lista2_2)
print("-----------------")
print(lista1[0:2])

lista1.append('Gorila gorila')  # Adiciona na lista
print(lista1)
lista1.remove('Homo sapiens')  # Remove da lista
print(lista1)
for item in lista2_2:  # Percorre uma lista
    print(item)

del(lista1)  # Deleta uma lista
