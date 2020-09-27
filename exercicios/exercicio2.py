import math
# Exercício 02 - PG 62

# Elabore um algoritmo que calcule a área de um círculo qualquer de raio fornecido.

raio = float(input("Digite o valor do raio: "))
area = (math.pi * (raio ** 2))

input(f'A area do circulo é: {area:.2f}')