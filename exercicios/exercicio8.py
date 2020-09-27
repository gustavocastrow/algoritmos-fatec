# Exercicio 2.5 PG 46-47

#Faça um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade e, também, verifique e
# mostre se ela já tem idade para votar ( 16 anos ou mais) e para conseguir a Carteira de Habilitação ( 18 anos ou mais).

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
calc_idade = 2020 - ano_nascimento


if calc_idade >= 18:
    print(f'Voce tem {calc_idade}, portanto pode votar e tirar CNH')
elif calc_idade >=16 and calc_idade <=18:
    print(f'Voce tem {calc_idade}, portanto pode votar, porem nao pode tirar cnh')
else:
    print(f'Voce tem {calc_idade}, ainda nao pode votar e nem ter CNH')


