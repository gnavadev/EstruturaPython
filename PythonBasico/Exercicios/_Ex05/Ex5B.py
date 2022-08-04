# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
# Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem,
# com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem,
# a distância percorrida e a quantidade de litros utilizada na viagem
# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# - Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# - Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)

# tempo gasto na viagem. velocidade media. DISTANCIA = TEMPO * VELOCIDADE. quantidade de litros de combustível. LITROS_USADOS = DISTANCIA / 12. O

def dados_usuario():
    tempo_gasto = float(input("Digite o tempo gasto na viagem: "))
    velocidade_media = float(input("Digite a velocidade media: "))
    return tempo_gasto, velocidade_media


def distancia(tempo_gasto_viagem, velocidade_media_viagem):
    distancia_total = tempo_gasto_viagem * velocidade_media_viagem
    return distancia_total


def litros(distancia_viagem):
    litros_viagem = distancia_viagem / 12
    return litros_viagem


def resultado(combustivel_gasto):
    print(f"Voce gastou {combustivel_gasto} litros")


dados = dados_usuario()
distancia_percorrida = distancia(dados[0], dados[1])
litros_gastos = litros(distancia_percorrida)
resultado(litros_gastos)
