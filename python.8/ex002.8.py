"""[Exercício 2] Escreva um programa que
mostre a tabuada de vários números, um
de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido
quando o número solicitado for negativo."""

while True:
    n = int(input("Qual tabuada você deseja ver? "))

    if n == 0:
        break
    else:
        print("="*30)
        print(f"TABUADA DO {n}")
        print("="*30)
        for a in range(1, 11):
            print(f"{a} x {n} = {a * n}")
