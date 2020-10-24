# Exercicio 15 PG-64

divisor = int(input("Informe o divisor: "))
dividendo = int(input("Informe o dividendo: "))
contador = 0;

while dividendo >= divisor:
    dividendo = dividendo - divisor;
    contador = contador +1
print(f'{contador}')