# Exercicio 17 PG-64

termo1 = int(input("Termo 1: "))
termo2 = int(input("Termo 2: "))
# termo1 = anterior
# termo2 = proxima


for n in range(0, 21):
    print(termo1)
    soma = termo2 + termo1
    termo1 = termo2
    termo2 = soma
