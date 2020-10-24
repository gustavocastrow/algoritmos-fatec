# Exercicio 10 PG-63

idade = int(input("Informe sua idade: "))

if idade < 16:
    print("Não votante")
elif idade >= 18 and idade <= 65:
    print("Eleitor Obrigatorio!")
elif idade >= 16 and idade < 18 or idade > 65:
    print("Voto facultativo")