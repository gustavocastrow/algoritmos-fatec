# Exercicio 31 PG-66

sexoM =  0 ; sexoF = 0 ; olhoAzul = 0
olhoVerde = 0
olhoCastanho = 0
cabeloLoiro = 0
cabeloCastanho = 0
cabeloPreto = 0
listaIdade = []
idade18a35homem = 0
idade18a35mulher = 0
idade = 0

while idade != -1:
    idade = int(input('Digite sua idade ou [ -1 ] para sair '))
    if idade ==-1:
        break;
    listaIdade.append(idade)
    sexo = input('Digite seu sexo M ou F ').upper()
    if sexo == 'F':
       sexoF = sexoF + 1
    elif sexo == 'M':
        sexoM += 1
        if idade > 17 and idade < 35:
            idade18a35homem += 1;


    olhos = input('Qual a cor dos seus olhos ').upper()
    if olhos == 'C':
            olhoCastanho += 1
    elif olhos == 'A':
             olhoAzul += 1
    elif olhos == 'V':
            olhoVerde += 1

    cabelo = input('Digite a cor dos seus cabelos ').upper()
    if cabelo =='L':
        if idade > 17 and idade < 35 and sexo == 'F':
            idade18a35mulher += 1
        cabeloLoiro += 1

    elif cabelo == 'C':
        cabeloCastanho += 1
    else:
        cabeloPreto +=1
listaIdade.sort()

print(f' {listaIdade[-1]} idade \n {cabeloPreto} cabelos Pretos \n {cabeloCastanho} cabelos castanhos  \n {cabeloLoiro} Cabelos loiros')
print (f'A maior idade dos habitantes foi {listaIdade[-1]} Anos')
print (f'  Percentagem de individuos masculino idade entre 18 e 35 foi {((100 * idade18a35homem ) / len(listaIdade)):.2f} % ')
print(f' Percentagem de indivíduos feminino idade entre 18 e 35 foi {((100* idade18a35mulher) / len(listaIdade)):.2f}')
