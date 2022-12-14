"""[Exercício 1] Escreva um programa que leia o
sexo de uma pessoa, mas só aceite ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente
até ter um valor correto."""

s = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
while s not in 'MF':
    print('RESPOSTA INVÁLIDA!')
    s = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]