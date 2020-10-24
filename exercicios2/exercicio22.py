# Exercicio 28 PG-64
# Construa um algoritmo que calcule o valor dos dez primeiros termos da série H, em que:
# H = 1/pot(1,3) - 1/pot(3,3) + 1/pot(5,3) - 1/pot(7,3) + 1/pot(9,3)

termo = int(input('Digite o termo '))
i =0
while i <= 10 :
    if i % 2 == 0:
        print('1/pot{},{} + '.format(termo, (3)), end=' ' )
    else:
        print('1/pot{},{} - '.format(termo, (3)), end=' ')
    i += 1
    termo+=2
