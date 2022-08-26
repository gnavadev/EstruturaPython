# 1 Constant
# log(n) Logarithmic
# n linear
# nlog(n) Log Linear
# n^2
# n^3
# 2^n Exponential

# %%
from math import log
from tkinter import N
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 100, 100)  # Gera numeros espacados de 1 a 10, 100 numeros
print(len(n))
print(n)

labels = ['Constant', 'Logarithmic', 'Linear',
          'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]


plt.figure(figsize=(10, 8))
plt.ylim(0, 5000)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
