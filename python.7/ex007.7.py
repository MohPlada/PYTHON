"""[Exercício 4] Escreva um programa que leia
um número e calcule seu fatorial mostra da
tela como exemplo a seguir. 5! = 5x4x3x2x1 = 120"""


m = int(input("Digite um número inteiro: "))
while m <= 0:
    print('NÃO EXISTE FATORIAL DE NÚMERO NEGATIVO OU ZERO!')
    m = int(input("Digite um número inteiro: "))
n = 1
print(f"{m}! = ", end='')
while m!= 0:
    if m != 1:
        print(f"{m}", end=' x ')
    else:
        print(f"{m}", end=' ')
    n *= m
    m -= 1
print(f'= {n}')