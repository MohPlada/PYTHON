"""[Exercício 4] Escreva um programa que
pergunte a distância de uma viagem em Km.
Calcule e peça o preço da passagem, cobrando
R$ 0,50 por Km para viagens de até 200Km e
R$ 0,45 para viagens mais longas."""

D = float(input("Quantos km foi percorrido na viagem?"))
if D <= 200:
    valor = D * 0.50
    print(f"O valor da passagem é {valor}..")
else:
    preço = D * 0.45
    print("O valor da passagem é {:.2f}.". format(preço))
