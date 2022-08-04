with open('Aulas\_14ManipulaArquivos\index.txt', 'r') as tex:
    r = tex.readlines()
    print(r)

with open('Aulas\_14ManipulaArquivos\index2.txt', 'w') as texto:
    texto.write("Ola a todos")
