""""Escreva um programa que leia duas notas do user e calcule a média. Se a média for maior que 7, retorne APROVADO. Caso contrário, retorne REPROVADO."""

print("*" * 20)
print("    CALCULADORA DE MÉDIAS")
print("*" * 20)

x = float(input("Digite sua primeira nota:"))
y = float(input("Digite sua segunda nota:"))
z = ((x+y)/2)
if z > 7:
    print("Você foi aprovado!")
else:
    print("Infelizmente tera que repetir!")
