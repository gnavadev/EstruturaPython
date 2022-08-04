# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
# utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário
# deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma,
# será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem,
# com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
# tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem


automovel = float(
    input('Digite quantos kilometros o automovel faz por litro: '))
tempo_gasto = float(input('Digite o tempo gasto na viagem: '))
velocidade_media = float(input('Digite a velocidade media: '))

distancia_percorrida = tempo_gasto * velocidade_media

litros_usados = distancia_percorrida / automovel

print(f'\n Velocidade media:{velocidade_media} \n Tempo Gasto:{tempo_gasto} \n Distancia Percorrida:{distancia_percorrida} \n Quantidade de litros:{litros_usados} \n')
