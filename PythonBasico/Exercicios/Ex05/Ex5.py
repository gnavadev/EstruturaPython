# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
# A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

def ler_temperatura():
    '''
    Recebe o valor de temperatura
    '''
    temperatura = float(input("Digite a temperatura em C: "))
    return temperatura


def calculo_temperatura(temperatura_celsius):
    '''
    Calcula a temperatura em celsius
    '''
    fahrenheit = (9 * temperatura_celsius + 160) / 5
    return fahrenheit


def resultado(temperatura, fahrenheit):
    '''
    Mostra o resultado da equacao
    '''
    print(f"{temperatura} em fahrenheit fica {fahrenheit}")


temperatura_c = ler_temperatura()
temperatura_f = calculo_temperatura(temperatura_c)
resultado(temperatura_c, temperatura_f)
