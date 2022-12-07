"""[Exercício 3] Escreva um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
import math

valor = float(input("Digite um valor:"))
print("O seno de {} é {}".format(valor, math.sin(valor)))
print("O cosseno de {} é {}".format(valor, math.cos(valor)))
print("A tangente de {} é {}".format(valor, math.tan(valor)))
