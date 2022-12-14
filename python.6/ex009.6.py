
"""[Exercício 9] Escreva um programa que leia
o ano de nascimento de sete pessoas. No final,
mostre quantas delas ainda não atingiram a
maioridade e quantas já são maiores."""

import datetime
maior = menor = 0
for i in range(1, 8):
    ano = int(input(f"{i}) Quantos anos você tem? "))
    idade = datetime.date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"{menor} ainda são demenor.")
print(f"{maior} são de maior.")