# Exercicio 27 PG-65

denominador = float(500)
soma = 0
s_d = 50

for c in range(2, 12):
    if c % 2 == 0:
        soma = soma + (2/denominador)
    else:
        soma = soma - (5/denominador)

    denominador -= s_d

    print(f'{soma}')