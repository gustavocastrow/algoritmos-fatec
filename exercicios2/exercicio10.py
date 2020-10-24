# Exercicio 16 PG-64

base = int(input("Infore a BASE: "))
expoente = int(input("Expoente: "))

potencia = 1;

for count in range(expoente):
    potencia *= base
    count += 1
print(base, "^", expoente, "=", potencia)