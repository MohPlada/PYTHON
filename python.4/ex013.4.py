"""[Exercício 8] Escreva um programa que leia o
comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo."""

i = float(input("Digite a primeira reta:"))
j = float(input("Digite a segunda reta:"))
k = float(input("Digite a terceira reta:"))

V1 = (i < j + k)
V2 = (j < i + k)
V3 = (k < i + j)

if i and j and k:
    print("TRIANGULO!")
else:
    print("NÃO É UM TRIÂNGULO!")
