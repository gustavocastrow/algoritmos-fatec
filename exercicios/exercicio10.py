# Exercicio 2.7 PG 46-47

# Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:

idade = int(input("Informe sua idade: "))

if idade < 5:
    print(f'Voce tem apenas {idade}, ainda nao se enquadra em uma categoria, aguarde ate 5 anos.')
elif idade >= 5 and idade <= 7:
    print(f'Voce tem {idade} anos, sua categoria é: INFANTIL A')
elif idade >= 8 and idade <= 10:
    print(f'Voce tem {idade} anos, sua categoria é: INFANTIL B')
elif idade >= 11 and idade <= 13:
    print(f'Voce tem {idade} anos, sua categoria é: JUVENIL A')
elif idade >= 14 and idade <= 17:
    print(f'Voce tem {idade} anos, sua categoria é: JUVENIL B')
elif idade >= 18:
    print(f'Voce tem {idade} anos, sua categoria é ADULTO')