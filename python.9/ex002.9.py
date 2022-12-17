"""[Exercício 2] Escreva um programa que uma tupla com
uma “lista de tops”. (Ex: Campeonato Brasileiro de Futebol,
ou os países que mais ricos do mundo e etc). Depois mostre:
1)	A penas os 5 primeiros colocados;
2)	Os últimos 4 colocados;
3)	Imprimir eles na tela com todos em ordem alfabética;"""

paises = ('marrocos', 'brasil', 'argentina', 'croacia', 'frança', 'japão', 'mexico')

print(f"Lista = {paises}")
print(f"Os preimeiros três colocados {paises[:3]}")
print(f"Os ultimos 4 colocados {paises[-4:]}")
print(f"Em ordem alfabética: {sorted(paises)}")

