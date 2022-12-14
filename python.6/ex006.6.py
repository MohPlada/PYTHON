"""[Exercício 6] Escreva um programa que
leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

i = int(input("Digite o primeiro termo:"))
j = int(input("Digite a razão de ums PA:"))
for k in range(i, i + 9 * j, j):
    print(k)
