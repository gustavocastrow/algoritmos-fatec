# Exercicio 16 PG-64
# Faça um algoritmo que seja capaz de obter o resultado de uma exponenciação para qualquer base e expoente inteiro
# fornecidos, sem utilizar a operação de exponenciação (pot)

base = int(input("Infore a BASE: "))
expoente = int(input("Expoente: "))

potencia = 1;

for count in range(expoente):
    potencia *= base
    count += 1
print(base, "^", expoente, "=", potencia)