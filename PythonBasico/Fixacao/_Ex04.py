nome = input("Digite o seu nome: ")
branco = 0

for i in range(len(nome)):
    print(nome[i])
    if nome[i] == " ":
        branco = branco + 1


print(f"Na string tem {branco} espacos em branco")
