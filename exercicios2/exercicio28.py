# Exercicio 34 PG-66

total = 100
otimo = 0
bom = 0
regular = 0
ruim = 0
pessimo = 0
total_idade = 0
total_idade_ruim = 0
maior_idade_otimo = 0
menor_idade_otimo = 0
menor_idade_ruim = 0
maior_idade_ruim = 0


for espectador in range(1, 100):
    print(f'<------- Espectador {espectador} ------->')
    idade = int(input('Qual sua idade?: '))
    opiniao = str(input(' [A] -> Ótimo \n [B] -> Bom \n [C] -> Regular \n [D] -> Ruim \n [E] -> Péssimo \n Qual sua opinião? : ')).upper()

    if opiniao == 'A':
        otimo = otimo + 1
        total_idade = total_idade + idade
        if espectador == 1:
            maior_idade_otimo = idade
        else:
            if idade > maior_idade_otimo:
                maior_idade_otimo = idade
            if idade < menor_idade_otimo:
                menor_idade_otimo = idade
    elif opiniao == 'B':
        bom = bom + 1
    elif opiniao == 'C':
        regular = regular + 1
    elif opiniao == 'D':
        ruim = ruim + 1
        total_idade_ruim = total_idade_ruim + idade

        if espectador == 1:
            maior_idade_ruim = idade
        else:
            if idade > maior_idade_ruim:
                maior_idade_ruim = idade
            if idade < menor_idade_ruim:
                menor_idade_ruim = idade

    elif opiniao == 'E':
        pessimo = pessimo + 1

    porcentagem_pessimo = pessimo / 100 * 100

    if maior_idade_ruim > maior_idade_otimo:
        diferenca_idade = maior_idade_ruim - maior_idade_otimo
    elif maior_idade_otimo > maior_idade_ruim:
        diferenca_idade = maior_idade_otimo - maior_idade_ruim


    media = total_idade_ruim / ruim


print(f'[1] A quantidade de respostas ótimo: {otimo}')
print(f'[3] A media de idade das pessoas que responderam ruim: {media:.2F}')
print(f'[4] A porcentagem das respostas pessimo e a maior idade que utilizou essa opcao: {porcentagem_pessimo} %')
print(f'[5] a diferença de idade entre a maior idade que responde otimo e a maior idade que respondeu ruim: {diferenca_idade}')


