# Exercicio 15 PG-64
# Faça um algoritmo que seja capaz de obter o quociente inteiro da divisão de dois números fornecidos, sem utilzar
# a operação de divisão (/) e nem a de divisão inteira (div).

divisor = int(input("Informe o divisor: "))
dividendo = int(input("Informe o dividendo: "))
contador = 0;

while dividendo >= divisor:
    dividendo = dividendo - divisor;
    contador = contador +1
print(f'{contador}')