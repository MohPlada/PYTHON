"""[Exercício 8] Escreva um programa que leia
uma frase qualquer e diga se ela é um PALÍNDROMO,
desconsiderando os espaços e a acentuação."""


i = str(input("Digite um frase: ")).strip().upper()
j = ''.join(i.split())
k = j[::-1]

if j == k:
    print("\033[mPALINDROMO\033[m")
else:
    print("\033[31mNÃO\033[m É UM \033[34mPALINDROMO\033[m")