"""[Exercício 6] Escreva um programa que leia
o nome completo de uma pessoa e mostre o
primeiro e o último nome separadamente."""

nome = str(input("Digite seu nome completo:"))
print("Seu primeiro nome é: {}".format(nome.split()[0]))
print("Seu último nome é: {}".format(nome.split()[-1]))