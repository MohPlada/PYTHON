"""[Exercício 5] Escreva um programa que
leia 6 números inteiros do usuário e
mostre a soma apenas daqueles que forem
pares, Se o valor for ímpar, desconsidere-o."""

soma = 0
for m in range(1, 7):
    n = int(input("Digite o valor:"))
    if n % 2 == 0:
        soma += n
        print(m)
