"""[Exercício 2] Escreva um programa que leia
a velocidade de um carro. Se ele ultrapassar 80 Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""

velocidade = int(input("Digite a quantos km você estava dirigindo:"))

if velocidade > 80:
    valor = (velocidade - 80) * 7
    print("Você foi multado,a cada km ultrapassado é cobrado R$7,00.")
    print(f"O valor ficara em {valor} reais.")
