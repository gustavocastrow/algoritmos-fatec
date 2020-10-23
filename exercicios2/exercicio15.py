# Exercicio 21 PG-64
# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por código. Os dados utilizados
# para a escrutinagem obedecem a seguinte condifição:
# 1, 2, 3, 4 = voto para os respectivos candidatos
# 5 = voto nulo
# 6 = voto em branco
# Elabore um algoritmo que calcule e escreva:
# -> O total de votos para cada canditado e seu percentual sobre o total
# -> O total de votos nulos e seu percentual sobre o total:
# -> O total de votos em branco e seu porcentual sobre o total:
# Como finalizador do conjunto de votos, tem-se o valor 0.

voto = 1
votos_candidato1 =  0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
nulo = 0
branco = 0
total = 0

while voto != 0:
    voto = int(input('Informe seu voto: \n [1] -> Candidato 01:   \n [2] -> Candidato 02:  \n [3] -> Candidato 03:  '
               '\n [4] -> Candidato 04:  \n [5] -> Nulo:  \n [6] -> Branco:  \n [0] -> Sair: '))
    if voto == 1:
        votos_candidato1 = votos_candidato1 + 1
        total = total + 1
    elif voto == 2:
        votos_candidato2 = votos_candidato2 + 1
        total = total + 1
    elif voto == 3:
        votos_candidato3 = votos_candidato3 + 1
        total = total + 1
    elif voto == 4:
        votos_candidato4 = votos_candidato4 + 1
        total = total + 1
    elif voto == 5:
        nulo = nulo + 1
        total = total + 1
    elif voto == 6:
        branco = branco + 1
        total = total + 1
print(f'O candidato 01 teve {votos_candidato1}, totalizando {votos_candidato1/total * 100:.2f}%')
print(f'O candidato 02 teve {votos_candidato2}, totalizando {votos_candidato2/total * 100:.2f}%')
print(f'O candidato 03 teve {votos_candidato3}, totalizando {votos_candidato3/total * 100:.2f}%')
print(f'O candidato 04 teve {votos_candidato4}, totalizando {votos_candidato4/total * 100:.2f}%')
print(f'Votos Nulos {nulo}, totalizando {nulo/total * 100:.2f}%')
print(f'Votos Branco {branco}, totalizando {branco/total * 100:.2f}%')
print(f'Votos Total  {total}')