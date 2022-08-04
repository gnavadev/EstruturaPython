import random
from secrets import choice

print(random.random())
print(random.randint(1, 10))
print(random.randrange(0, 10, 2))  # Comeco, Fim , Step
print(random.randrange(0, 10, 3))  # Comeco, Fim , Step

X = ['K', 'd', 13, '34-j', 'x']

print(random.choice(X))
