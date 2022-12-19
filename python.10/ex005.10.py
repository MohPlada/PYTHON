"""[Exercício 6] [DESAFIO] Escreva um programa que o usuário
digite uma expressão matemática qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta."""

i = list()
expressao = str(input("Digite a expressão: ")).upper().strip().split()
expressao = ''.join(expressao)
for simbolo in expressao:
    if simbolo == '(':
        i.append(simbolo)
    elif simbolo == ')':
        if len(parenteses) > 0:
            i.pop()
        else:
            i.append(')')
            break
if len(i) == 0:
    print("Sua expressão está \033[034mCORRETA\033[m!")
else:
    print("Sua expressão está \033[031mERRADA\033[m!")