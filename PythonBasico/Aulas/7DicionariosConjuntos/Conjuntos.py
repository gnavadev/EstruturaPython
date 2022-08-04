biomoleculas = ("Proteina", "Acidos Nucleios", "Carboidrato", "Lipideos",
                "Acidos Nucleios", "Carboidrato", "Carboidrato", "Carboidrato")
print(biomoleculas)
print("---------------------")
print(set(biomoleculas))  # Traz o conjunto sem items repetidos
print("---------------------")

c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
c3 = c1.intersection(c2)

print(c3)

print(c1.difference(c2))  # Mostra as diferencas entre c1 e c2
