"""[Exercício 3] Escreva um programa que vai
gerar cinco números aleatórios e colocar
dentro em uma tupla. Depois disso, mostre a
listagem de números gerados e também indique
o menor e o maior valor que estão na tupla."""

import random

aleatorio = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
             random.randint(1, 10), random.randint(1, 10))

print(aleatorio)
for a in range(0, 5):
    if a == 0:
        maior = menor = aleatorio[0]
    else:
        if aleatorio[a] > maior:
            maior = aleatorio[a]
        if aleatorio[a] < menor:
            menor = aleatorio[a]
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")
