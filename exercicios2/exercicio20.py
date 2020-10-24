# Exercicio 26 PG-65

termo = int(input('Digite o termo '))
i =0
while i <= 10 :
    print('{}/{} + '.format(termo, (termo*termo)), end=' ' )
    i += 1
    termo+=1
