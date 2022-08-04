# Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)

tabuada = int(input("Digite o numero desejado: "))
multiplicador = 1
while multiplicador <= 10:
    resultado = tabuada * multiplicador
    print(f"{tabuada} X {multiplicador} = {resultado}")
    multiplicador += 1
