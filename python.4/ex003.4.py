"""Escreva um programa que leia uma string e retorne um “bom dia” ao user, dizendo que o nome dele é bonito caso o nome começar com a letra A."""

a = str(input("Olá,qual o seu nome?")).strip()
if a.lower()[0] == "a":
    print("Seu nome é lindissimo!!!")
print(F"Bom dia {a}!")