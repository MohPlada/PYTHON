"""[Exercício 2] Escreva um programa que leia um número
entre 0 e 9999 e mostre cada um dos dígitos separados
mostrando quantas unidades, dezenas, centenas e milhares há nesse número."""

number = int(input("Digite um número de 0 a 9999:"))
i = str(int(10000 + number))
print("Milhares: {}".format(i[1]))
print("Centenas: {}".format(i[2]))
print("Dezenas: {}".format(i[3]))
print("Unidades: {}".format(i[4]))