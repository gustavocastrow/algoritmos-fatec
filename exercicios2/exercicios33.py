#Realizou-se uma pesquisa para determinar alguns dados estatísticos em relação ao conjunto de crianças nascidas em um certo
# periodo de uma determinada maternidade.
# Construa um algoritmo que leia o
# número de crianças nascidas nesse período e, depois,
# em um número indeterminado de vezes, o sexo de um recém-nascido prematuro ('M' - masculino ou 'F' - feminino) e o numero
# de dias que este foi mantido na incubadora. Como finalizador, teremos a letra 'X' no lugar do sexo da criança.
# Determine e imprima:
#• a porcentagem de recem-nascidos prematuros;
#• a porcentagem de recem-nascidos meninos e meninas do total de prematuros:
#• a média de dias de permanència dos recém-nascidos prematuros na incubadora:
#• o maior número de dias que um recém-nascido prematuro permaneceu na incubadora:

prematuros = 0
recemNascidoF = 0
recemNascidoM = 0
diasIncubadora = []
criancas = 0
continua = str
sexo = str


while continua != 3:
        criancas = int(input('O bebe que nasceu é prematuro ? [1] - SIM [2] NAO OU [3] para Sair '))
        if criancas == 3:
            break;
        if criancas == 1:
            diasIncubadora.append(int(input('Quantos dias ficou na incubadora ?')))
            prematuros += 1
        elif criancas == 2:
            sexo = input('É do sexo [M]asculino ou [F]eminino ? ').upper()
            if sexo =='F':
              recemNascidoF += 1
            elif sexo =='M':
                recemNascidoM += 1
        criancas += 1

print(f'Total de Recém nascidos Masculinos {recemNascidoM} \n Total de recém nascidos Femininos {recemNascidoF} \n Total de prématuro {prematuros}')
##A porcentagem de recem-nascidos prematuros;
print(f' A porcentagem de recém-nascidos prematuros foi de {(100 * prematuros) / criancas:.0f}% ')
#• a porcentagem de recem-nascidos meninos e meninas do total de prematuros:
print(f'a Porcentagem de recém-nascidos meninos e meninas foi de {((recemNascidoM+recemNascidoF)*100) / prematuros :.0f}%')
#o maior número de dias que um recém-nascido prematuro permaneceu na incubadora:
diasIncubadora.sort()
print(f' O maior dias que um recém nascido prematuro ficou na incubadora foi {diasIncubadora[-1]} dias')
#• a média de dias de permanència dos recém-nascidos prematuros na incubadora:
print(f' A média de dias na incubadora foram de {sum(diasIncubadora) / len(diasIncubadora)}')

