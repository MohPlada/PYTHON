"""[Exercício 3] Escreva um programa que
leia o nome de uma cidade e informe se
ela começa com a palavra “Santo”."""

cidade = str(input("Digite o nome da cidade:")).strip()
print("A cidade começa com a palavra 'SANTO'? {}".format("SANTO" in cidade.split()[0].upper()))