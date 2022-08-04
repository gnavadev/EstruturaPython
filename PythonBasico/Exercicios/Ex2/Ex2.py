# Leia a idade do usuário e classifique-o em:
# - Criança – 0 a 12 anos
# - Adolescente – 13 a 17 anos
# - Adulto – acima de 18 anos
# -Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida


idade_usuario = int(input("Insira a sua idade: "))

if idade_usuario > 0 and idade_usuario <= 12:
    print("\n Crianca \n")
else:
    if idade_usuario > 12 and idade_usuario <= 17:
        print("\n Adolescente \n")
    else:
        if idade_usuario >= 18:
            print("\n Adulto \n")
        else:
            print("\n Idade Invalida \n")
