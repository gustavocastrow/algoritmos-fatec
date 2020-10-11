# Exercicio 10 PG-63
# A partir da idade informada de uma pessoa, elabora um algoritmo que informe sua classe eleitoral, sabendo que
# menores de 16 não votam (não votante), que o voto é obrigatorio para adultos entre 18 e 65 anos (eleitor obrigatorio)
# e que o voto é opcional para eleitores entre 16 e 18 anos ou maiores de 65 anos(eleitor facultativo)

idade = int(input("Informe sua idade: "))

if idade < 16:
    print("Não votante")
elif idade >= 18 and idade <= 65:
    print("Eleitor Obrigatorio!")
elif idade >= 16 and idade < 18 or idade > 65:
    print("Voto facultativo")