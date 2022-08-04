# Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo,
# crie uma estrutura de repetição para percorrer cada elemento do dicionário para
# gravar cada aluno em um novo arquivo de texto
# - Cada aluno deve ocupar uma linha do novo arquivo de texto
# - O formato deve ser: nome,nota (Pedro,8.0)
# - Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('Exercicios\_Ex08\index2.txt', 'w') as texto:
    for aluno, nota in alunos.items():
        texto.write(f"Aluno:{aluno} Nota: {nota} \n")

with open('Exercicios\_Ex08\index2.txt', 'r') as tex:
    r = tex.readlines()
    print(r)
