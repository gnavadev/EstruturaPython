# Ler 5 notas e informar a média
nota_contador = 0
nota_total = 0
while nota_contador < 5:
    nota_aluno = float(input("Digite uma nota: "))
    nota_total = nota_total + nota_aluno
    nota_contador += 1
nota_final = nota_total / 5
print(f"Sua nota final foi: {nota_final}")
