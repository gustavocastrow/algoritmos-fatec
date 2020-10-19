'''ELABORE UM ALGORITMO QUE IMPRIMA TODOS OS NUMEROS PRIMOS EXISTENTES
ENTRE N1 E N2, EM QUE N1 E N2 SAO NUMEROS NATURAIS FORNECIDOS PELO USUARIO'''

n1 = int (input('Digite o primeiro numero '))
n2 = int (input('Digite o segundo numero '))

for i in range(n1, n2+1):
    if n2 % i ==0:
      print('{}'.format(i), end=' ')
