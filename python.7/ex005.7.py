"""[Exercício 2] Escreva um programa que o computador vai “pensar”
em um número inteiro entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar o número, mostrando no final quantos
palpites foram necessários para vencer."""

import random
computador = random.randint(0, 10)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Digite um valor: '))
    cont += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {cont} tentativas')