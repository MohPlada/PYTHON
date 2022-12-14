""" Escreva um programa que escreva “Hello, world!” na tela, enquanto o usuário quiser."""

resposta = "S"
while resposta == "S":
    j = str(input("Digite sua frase:"))
    resposta = str(input("Deseja continuar? [S / N] ")).upper()
print("********")