"""[Exercício 7] Refaça o exercício 6, mas acrescentando se o
triângulo, caso seja formado, é: EQUILÁTERO, ISÓCELES ou ESCALENO."""

L1 = float(input("DIgite o valor:"))
L2 = float(input("DIgite o valor:"))
L3 = float(input("DIgite o valor:"))

i = (L1 < L2 + L3)
j = (L2 < L1 + L3)
k = (L3 < L2 + L1)

if i and j and k:
    print("TRIANGULO")
    if i == j == k:
        print("EQUILATERO")
    elif i != j != k:
        print("ESCALENO")
    else:
        print("ISÓCELES")
else:
    print("nÃO É UM TRIANGULO")