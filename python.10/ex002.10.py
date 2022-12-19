"""[Exercício 3] Escreva um programa que o user
digite 5 valores numéricos e cadastre-os em
uma lista, já na posição correta de inserção
(SEM USAR O sort()). No final, mostre a lista ordenada na tela."""

valores = list()

for a in range(0, 5):
    valor = int(input("Digite um valor: "))
    if a == 0 or valor > valores[-1]:
        valores.append(valor)
        print("Adicionado ao final da lista.")
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                print(f"Adicionado na posição {posicao} da lista.")
                break
            posicao += 1
print(valores)
