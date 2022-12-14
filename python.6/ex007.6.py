"""[Exercício 7] Escreva um programa que leia
um número inteiro e diga se ele é primo ou não."""

a = int(input("Digite um numero inteiro:"))
contador = 0

for b in range(1, a + 1):
    if a % b == 0:
        contador += 1
if contador == 2:
    print("PRIMO")
else:
    print("NAO É PRIMO")