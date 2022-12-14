"""[Exercício 4] Escreva um programa que leia
duas notas do aluno, calcule a sua média e diga:
1)	Média abaixo de 5: REPROVADO
2)	Entre 5 e 6.9: RECUPERAÇÃO
3)	Acima de 7: APROVADO"""

a = float(input("Digite sua primeira nota:"))
b = float(input("Digite sua segunda nota:"))
media = (a + b) / 2

if media > 7:
    print("APROVADO!!!")
elif 5 <= media < 6.9:
    print("RECUPERAÇÃO!")
else:
    print("REPROVADO")
