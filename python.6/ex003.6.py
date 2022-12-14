"""[Exercício 3] Escreva um programa que calcule a
soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo de 1 até 500."""

soma = 0
for a in range(1,501):
    if a % 2 != 0 and a % 3 == 0:
        soma =+ 1
        print(a)
print("Fim")