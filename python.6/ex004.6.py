
"""[Exercício 4] Escreva um programa que leia
um número do usuário e retorne a tábuada desse número."""

t = int(input("Digite o número:"))
for i in range (1,11):
    print(f"{i} x {t} = {i*t}")
