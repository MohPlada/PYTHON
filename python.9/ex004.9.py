"""[Exercício 4] Escreva um programa que leia 4 valores
pelo teclado e guarde-os em uma tupla. No final, mostre:
1)	Quantas vezes apareceu o valor 9;
2)	Em que posição foi digitado o primeiro valor 3;
3)	Quais foram os números pares.
Lembrando que, se o usuário digitar uma valor que não
esteja na tupla, precisa retornar erro."""

perguntas = (int(input("Digite um número: ")), int(input("Digite um número: ")),
             int(input("Digite um número: ")), int(input("Digite um número: ")))

print(f"O número nove apareceu {perguntas.count(9)} vezes.")

if 3 in perguntas:
    print(f"Primeira posição do 3 foi na tupla {perguntas.index(3)}.")
else:
    print("O valor 3 não foi digitado.")
print("Os valores pares digitados foram:", end='')
for m in perguntas:
    if m % 2 == 0:
        print(m, end=' ')
