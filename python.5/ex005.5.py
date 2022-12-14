"""[Exercício 6] Escreva um programa que leia os 3 lados
de um triângulo e diga se eles formam ou não um triângulo."""

L1 = float(input("DIgite o valor:"))
L2 = float(input("DIgite o valor:"))
L3 = float(input("DIgite o valor:"))

i = (L1 < L2 + L3)
j = (L2 < L1 + L3)
k = (L3 < L2 + L1)

if i and j and k:
    print("TRIANGULO")
else:
    print("nÃO É UM TRIANGULO")