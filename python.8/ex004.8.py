"""[Exercício 3] Escreva um programa que
jogue par ou impar com o computador.
O jogo só será interrompido quando o
jogador PERDER, mostrando o total de
vitórias consecutivas que ele conquistou
no final do jogo."""

import random

contador = 0

while True:
    print("PAR OU ÍMPAR")
    print("¨" * 15)
    print("(1) - PAR")
    print("(2) - IMPAR")
    opcao = int(input("Escolha a opção:"))
    while opcao != 1 and opcao != 2:
        print("OPÇÃO INVÁLIDA!!")
        opcao = int(input("Escolha a opção:"))

    numero = int(input("Digite o número:"))
    computador = random.randint(1, 100)
    soma = numero + computador

    if opcao == 1 and soma % 2 == 0:
        print("VOCÊ VENCEU!")
        contador += 1
    else:
        print("VOCÊ PERDEU!")
        break

print("FINISH")
print(f"Você tem {contador} vitórias consecutivas.")

