"""[Exercício 7] Escreva um programa que pergunte
o salário de um funcionário e calcule o valor
do seu aumento. Para salários superiores a R$1.250,00,
calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%."""

s = float(input("Qual o valor do seu salário?"))
if s > 1250:
    print("Seu salário aumentou para R$ {:.2f}.".format(s * 1.1))
else:
    print("Seu salàrio aumentou para R$ {:.2f}.".format(s * 1.15))
