"""[Exercício 2] Escreva um programa que leia um número
inteiro qualquer e peça ao usuário qual será a base de conversão:
1)	[1] – Binário
2)	[2] – Octal
3)	[3] - Hexadecimal"""

i = int(input("Digite um número inteiro:"))

print("-" * 20)
print("""Escolha uma das bases para conversão:
[1] - BINÁRIO
[2] - OCTAL
[3] - HEXADECIMAL""")
print("-" * 20)

escolha = int(input("Digite a o escolhido:"))

if escolha == 1:
    print(f"{i} em BINÁRIO = {bin(i)[2:]}")
elif escolha == 2:
    print(f"{i} em OCTAL = {oct(i)[2:]}")
elif escolha == 3:
    print(f"{i} em HEXADECIMAL = {hex(i)[2:]}")
else:
    print("OPÇÃO INVÁLIDA!")
