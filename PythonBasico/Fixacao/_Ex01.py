
# %%

valorEmReais = float(input("Digite um valor em reais: "))
notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0

while valorEmReais > 0:
    if valorEmReais >= 100:
        notas100 = notas100 + 1
        valorEmReais = valorEmReais - 100
    elif valorEmReais >= 50 and valorEmReais < 100:
        notas50 = notas50 + 1
        valorEmReais = valorEmReais - 50
    elif valorEmReais >= 10 and valorEmReais < 50:
        notas10 = notas10 + 1
        valorEmReais = valorEmReais - 10
    elif valorEmReais >= 5 and valorEmReais < 10:
        notas5 = notas5 + 1
        valorEmReais = valorEmReais - 5
    elif valorEmReais >= 1 and valorEmReais < 5:
        notas1 = notas1 + 1
        valorEmReais = valorEmReais - 1


print(f"Total: {notas100} notas de 100 || {notas50} notas de 50 || {notas10} notas de 10 || {notas5} notas de 5 || {notas1} notas de 1")
