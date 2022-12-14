"""[Exercício 3] Escreva um programa que leia dois números
inteiros e compare-os, mostrando na tela a mensagem:
1)	“O primeiro valor é maior”
2)	“O segundo valor é maior”
3)	“Não existe valor maior, ambos são iguais”"""

i = int(input("Digite o primeiro número inteiro:"))
j = int(input("Digite o segundo número inteiro:"))

menor = i < j and i or j
maior = i > j and i or j

if menor == maior:
    print ("São iguais!")
else:
    print(i > j and f"O {i} é maior." or f"{j} é maior." )