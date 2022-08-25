
# %%
vetor1 = [int(input("Digite um numero: ")) for x in range(10)]
vetor2 = [int(input("Digite um numero: ")) for y in range(10)]
vetor3 = [vetor1[z] + vetor2[z] for z in range(10)]


print(vetor3)
