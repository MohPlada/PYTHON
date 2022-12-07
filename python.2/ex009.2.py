"""[Exercício 5] Escreva um prorgama que leia o nome de 4 alunos
e coloque eles em uma ordem aleatória, monstrando essa ordem na tela."""

import random

p1 = input("Digite o primeiro nome:")
p2 = input("Digite o segundo nome:")
p3 = input("Digite o terceiro nome:")
p4 = input("Digite o quarto nome:")
lista = [p1, p2, p3, p4]
random.shuffle(lista)
print("A ordem da lista é: {}".format(lista))
