# Exercicio 23 PG-64
# Elabore um algoritmo que imprima todos os numeros primos existentes entre N1 e N2 em que N1 e N2 são números
# naturais fornecidos pelo usuário
# Numeros naturais -> Numeros inteiros positivos (não-negativos) ex -> {0,1,2,3,4,5,6}

num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")


n1 = int(input('Informe o primeiro numero:'))
n2 = int(input('Informe o segundo número: '))

