"""[Exercício 1] Escreva um programa que
o computador pensará em um número entre 0 e 5.
Em seguida, o usuário deverá adivinhar esse valor.
Caso o usuário acerte, retorne “VENCEU”, caso perca, retorne “PERDEU”."""

import random

print("=" * 20)
print("  JOGO DO ADVINHA")
print("=" * 20)
j = input("Você pode escolher um número de 0 a 5.Digite seu número:")
i = random.randint(0,5)
if j == i:
    print("Parabéns você GANHOU!")
else:
    print("Você PERDEU!")
