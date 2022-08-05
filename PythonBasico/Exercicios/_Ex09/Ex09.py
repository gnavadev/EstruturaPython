# Crie uma classe chamada aluno com os seguintes atributos:
# - Nome
# - Nota 1
# - Nota 2
# - Crie um construtor para a classe (__init__)

# Crie as seguintes funções (métodos):
# - Calcula média, retornando a média aritmética entre as notas
# - Mostra dados, que somente imprime o valor de todos os atributos
# - Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)

# Crie dois objetos (aluno1 e aluno2) e teste as funções

class Alunos:
    def __init__(self, nome, nota, nota2):
        self.nome = nome
        self.nota = nota
        self.nota2 = nota2
        self.media = 0.0  # Media nao esta nos parametros
        # Porque nao vai ser passada pelo usuario

    def calcula_media(self):
        self.media = (self.nota + self.nota2) / 2
        return self.media

    def mostradados(self):
        print('Nome: ', self.nome)
        print('Nota1: ', self.nota)
        print('Nota2: ', self.nota2)

    def resultado(self):
        if self.media >= 6.0:
            return("Aluno Aprovado")
        else:
            return("Aluno Reprovado")


aluno1 = Alunos('Gabriel', 10.0, 10.0)
media1 = aluno1.calcula_media()
aluno1.mostradados()
print(media1)
print(aluno1.resultado())

aluno2 = Alunos('ZE', 5.0, 4.0)
media2 = aluno2.calcula_media()
aluno2.mostradados()
print(media2)
print(aluno2.resultado())
