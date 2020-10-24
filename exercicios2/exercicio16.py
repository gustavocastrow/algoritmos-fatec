# Exercicio 22 PG-64

contador = 0
for dado1 in range(1, 7):
    for dado2 in range(1, 7):
        soma = dado1 + dado2
        if soma == 7:
            contador += 1
print(contador)
