# Exercicio 26 PG-64
# Elabora um algoritmo que determine o valor de S em que:  H= 1/1 + 3/2 + 4/6 + 5/25 + 6/36.. 10/100

# Exercicio 26 PG-64
# Elabora um algoritmo que determine o valor de S em que:
# H= 1/1 + 2/4 + 3/9 + 4/16 + 5/25 + 6/36.. 10/100


termo = int(input('Digite o termo '))
i =0
while i <= 10 :
    print('{}/{} + '.format(termo, (termo*termo)), end=' ' )
    i += 1
    termo+=1
