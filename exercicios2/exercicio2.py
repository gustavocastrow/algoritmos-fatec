# Exercicio 8 PG-63
# Elabore um algoritmo que, a partir de um dia, mês e ano fornecidos, valide se eles compõem uma data válida.
# Não deixe de considerar os meses com 30 ou 31 dias, e o tratamento de ano bissexto.

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mes: "))
ano = int(input("Informe o ano: "))

data_valida = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        data_valida = True
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        data_valida = True
elif mes == 2:
    if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
        if dia <= 29:
            data_valida = True
        elif dia <= 28:
            data_valida = True
if data_valida:
    print("Data válida!")
else:
    print("Data inválida!")