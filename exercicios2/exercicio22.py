# Exercicio 28 PG-65

termo = int(input('Digite o termo '))
i =0
while i <= 10 :
    if i % 2 == 0:
        print('1/pot{},{} + '.format(termo, (3)), end=' ' )
    else:
        print('1/pot{},{} - '.format(termo, (3)), end=' ')
    i += 1
    termo+=2
