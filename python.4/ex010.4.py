"""[Exercício 5] Escreva um programa que
leia um ano qualquer e mostre se ele é BISSEXTO."""

ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Bissexto')
else:
    print('Não é bissexto')
