# Faça uma lista que tenha 100 números aleatórios entre 0 a 100!
import random

lista = []
for i in range(100):
    radom = random.randint(0, 100) 
    lista.append(radom)
print(lista)


