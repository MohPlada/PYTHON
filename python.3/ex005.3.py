"""[Exercício 5] Escreva um programa que leia um frase e mostre:
1)	Quantas vezes aparece a letra “A”;
2)	Em que posição ela aparece pela primeira vez;
3)	Em que posição aparece pela última vez."""

frase = input("Escreva uma frase:")
print("A letra 'a' aparece {} vezes na sua frase.".format(frase.count("a")))
print("A letra 'a' aparece pela primeira vez na posição: {}".format(frase.lower().find("a")))
print("E pela ultima vez ela aparece na posição: {}".format(frase.lower().rfind("a") + 1))
