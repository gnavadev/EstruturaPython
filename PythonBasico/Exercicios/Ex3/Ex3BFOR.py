# Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)

tabuada = int(input("Digite o numero desejado: "))
for multiplicador in range(1, 11):
    resultado = tabuada * multiplicador
    print(f"{tabuada} X {multiplicador} = {resultado}")
