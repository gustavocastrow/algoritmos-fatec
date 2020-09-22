import math as m

tipo = input("Informe Q - Quadrado ou C - Circulo: ")
valor = float(input("Informe o valor do raio ou lado da figura: "))

area = 0.0

if tipo.lower() == 'c':
    area = m.pi * (valor ** 2)
    print("Tipo: {} - Lado: {:.2f} - Are: {:.2f}".format(tipo.upper(), valor, area))
elif tipo.lower() == 'q':
    area = valor * valor
    print("Tipo: {} - Lado: {:.2f} - Are: {:.2f}".format(tipo.upper(), valor, area))
else:
    print("Informe um tipo valido")