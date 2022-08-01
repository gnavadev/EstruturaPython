a = 'casaco'
maiuscula = a.upper()
print(maiuscula)
minuscula = maiuscula.lower()
print(minuscula)
capital = minuscula.capitalize()
print(capital)
# Posicao zero ate 3 , vai retornar Cas, indice 0 1 e 2
metade_palavra = a[0:3]
print(metade_palavra)
ultimas_letras = a[3:]  # Busca A da posicao 3 pra frente
print(ultimas_letras)
b = a.replace('aco', 'inha')  # b recebe a com inha no lugar de aco
print(a)
print(b)
c = a.replace('o', 'a')
print(c)
print(c.find('s'))  # Resultado sera 2, porque S esta na posicao 2 de casaca
print(c.find('a'))  # Resultado sera 1, porque p primeiro A esta na posicao 1
e = ' casaco '
print(len(e))  # Resultado sera 8, porque tem 6 letras e 2 espacos em branco
f = e.strip()  # Retira os espacos de da variavel e ' casaco '
print(f)
print(len(f))  # Resultado ser 6, porque foram removidos os espacos de ' casaco '
n1 = 14
n2 = 16

# F indica formatacao, isso seria bem parecido com as template strings do javascript
print(f'Didindo {n1} por {n2} o resultado eh {n1/n2}')
