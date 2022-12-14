"""Escreva um programa que o usuário escreverá quantos números ele quiser. No final, mostre quantos valores pares e impares
foram digitados ao total."""

par = 0
impar = 0
resposta = "S"
while resposta == "S":
    numero = int(input("Digite um valor:"))

    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    resposta = str(input("Deseja continuar? [S / N]")).upper()
print(f"Você digitou o valor {par}  pares e {impar} impares. ")
