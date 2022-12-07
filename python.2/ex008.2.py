import random
N1 = str(input("1o aluno: "))
N2 = str(input("2o aluno: "))
N3 = str(input("3o aluno: "))
N4 = str(input("4o aluno: "))
lista = [N1, N2, N3, N4]
random.shuffle(lista)
print("A ordem da lista é: {}".format(lista))
