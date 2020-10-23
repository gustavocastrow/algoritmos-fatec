#ELABORE UM ALGORITMO QUE IMPRIMA TODOS OS NUMEROS EXISTENTES ENTRE N1 E N2,
#EM QUE N1 E N2 SAO NUMEROS NATURAIS FORNECIDOS PELO USUARIO

n1= int (input('Digite o valor do primeiro numero '))
n2= int (input('Digite o valor do segundo numero '))

print(f'  Os numeros primos no intervalor digitado de {n1} e {n2} foram :')

for i in range (n1,n2):
    j= 2
    counter = 0
    while j < i:
        if i % j ==0:
            counter = 1
            j = j +1
        else:
            j = j+1

    if counter ==0:

        print(str(i), end=' ')
    else:
        counter = 0