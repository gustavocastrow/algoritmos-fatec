# Exercicio 2.2 PG 46-47

# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.
# Utilize para tal uma seleção encadeada.

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceirot valor: "))

if valor1 > valor2 > valor3:
    print(valor1, valor2, valor3)
if valor1 > valor3 > valor2:
    print(valor1, valor3, valor2)
if valor2 > valor1 > valor3:
    print(valor2, valor1, valor3)
if valor2 > valor3 > valor1:
    print(valor2, valor3, valor1)
if valor3 > valor1 > valor2:
    print(valor3, valor1, valor2)
if valor3 > valor2 > valor1:
    print(valor3, valor2, valor1)
if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print("Invalido")

# Forma mais simples de ser revolvido usando array e sorted.
#lista=[valor1, valor2, valor3]
# print(sorted(lista))