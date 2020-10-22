# Exercicio 17 PG-64
# Construa um algoritmo que gere os primeiros 20 termos de uma série tal qual a de Fibonacci,
# mas cujos os 2 primeiros termos sejam fornecidos pelo usuário

termo1 = int(input("Termo 1: "))
termo2 = int(input("Termo 2: "))
# termo1 = anterior
# termo2 = proxima


for n in range(0, 21):
    print(termo1)
    soma = termo2 + termo1
    termo1 = termo2
    termo2 = soma
