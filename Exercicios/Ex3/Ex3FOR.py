# Ler 5 notas e informar a média

nota_total = 0

for nota_contador in range(0, 5):
    nota_aluno = float(input("Digite uma nota: "))
    nota_total = nota_total + nota_aluno
nota_final = nota_total/5
print(f"Sua nota foi: {nota_final}")
