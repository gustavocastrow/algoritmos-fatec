# Exercicio 23 PG-65

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
contador = 0
primo = 0
for i in range(num1, num2 + 1):
    if num1 % i == 0:
        contador += 1

    if num2 % i == 0:
        contador += 1

print(f'Entre {num1} e {num2} temos {contador} numeros primos.')

