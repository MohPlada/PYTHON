print ("*-*" * 12)
print("     CALCULADORA DE MÉDIAS")
print ("*-*" * 12)

nome = input("Olá,qual o seu nome?")
n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
print("Olá {}, sua média foi {}.".format(nome,(n1+n2)/2))