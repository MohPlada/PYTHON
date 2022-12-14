maior = 0

"""[Exercício 10] Escreva um programa que leia
o peso de cinco pessoas. No final, mostre
qual foi o maior e menor peso lidos."""


menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}o pessoa: '.format(p)))

    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido é {}'.format(maior))
print('O menor peso lido é {}'.format(menor))