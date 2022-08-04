import math

a = 5
b = 3
print(a, b)
print("A soma eh: ", a + b)
print("A subtracao eh: ", a - b)
print("A divisao eh: ", a / b)
print("A multiplicacao eh: ", a * b)
print("O resto da divisao eh: ", a % b)
print('5 Elevado a 3 eh: ', 5**3)
print(math.sqrt(81))
# Arredondamento
casos_doenca = 134
numero_habitantes = 34432
casos_por_habitante = casos_doenca / numero_habitantes
# Arredonda para 3 casas depois da virgula
casos_por_habitante_arredondado = round(casos_por_habitante, 3)
print(casos_por_habitante_arredondado)
