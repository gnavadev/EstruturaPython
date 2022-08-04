coleta = {"Aedes aegypt": 32, "Aedes albopictus": 22, "Anopheles darlingi": 14}
print(coleta["Aedes aegypt"])  # Retorna a quantidade do elemento
coleta["Rhodnius montegrensis"] = 11  # Adicionado no Dicionario
print(coleta)
del(coleta)["Aedes albopictus"]  # Retira do Dicionario
print(coleta)
print("----------------------------")
print(coleta.items())  # Mostra tudo do dicionario
print("----------------------------")
print(coleta.keys())  # Mostra as chaves ou nomes do dicionario
print("----------------------------")
print(coleta.values())  # Mostra os valores das chaves do dicionario
print("----------------------------")
coleta2 = {"Anopheles gambiae": 13, "Anopheles deanorum": 14}
print(coleta2)
print("----------------------------")
coleta.update(coleta2)  # Atualiza utilizando os dados passados.
print(coleta)
for especie, num_especimes in coleta.items():
    print(
        f"Especie: {especie}, Numero de especimes coletados: {num_especimes}")
