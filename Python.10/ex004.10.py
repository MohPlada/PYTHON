"""[Exercício 5] Escreva um programa que :
1) vai ler vários valores numéricos e colocá-los em uma lista.
2) Crie duas listas extras que vão conter:
  2.1) Apenas os valores pares e ímpares digitados, respectivamente.
3) No final, mostre as 3 listas."""

numeros = list()
pares = list()
impares = list()
while True:
    auxiliar = int(input("Digite um valor: "))
    numeros.append(auxiliar)
    if auxiliar % 2 == 0:
        pares.append(auxiliar)
    elif auxiliar % 2 != 0:
        impares.append(auxiliar)
    resposta = str(input("Deseja continuar[S/N]?")).upper()
    while resposta not in 'SN':
        resposta = str(input("RESPOSTA INVÁLIDA!\nDeseja continuar[S/N]?")).upper()
    if resposta == 'N':
        break

print(f"Você digitou a seguinte lista = {numeros}")
if len(pares) == 0:
    print("Nenhum valor par foi digitado.")
else:
    print(f"Nessa lista, os seguintes números eram pares: {pares}")
if len(impares) == 0:
    print("Nenhum valor ímparfoi digitado.")
else:
    print(f"Nessa lista, os seguintes números eramímpares: {impares}")
