# Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição.
# Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média

notas = {}
media = 0
for j in range(1, 4):
    nome_aluno = str(input("Digite o Nome do Aluno: "))
    nota_aluno = float(input("Digite a nota do aluno: "))
    notas[nome_aluno] = nota_aluno
print(notas.items())

for nome, nota in notas.items():
    media = media + nota
media = media / 3
print(media)
