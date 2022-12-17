"""[Exercício 5] Escreva um programa que
tenha uma tupla única com os nomes de
produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem
de preços, organizando os dados em forma tabular."""

print("-" * 20)
print("VALORES DA FRUTEIRA")
print("-" * 20)
produtos = ('maça', 2.00, 'pera', 6.00, 'abacaxi', 5.00, 'uva', 12.00)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f"{produtos[posicao]:.<23}", end='')
    else:
        print(f"R$ {produtos[posicao]:.2f}")
