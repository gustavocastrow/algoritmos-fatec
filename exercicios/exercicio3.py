# Exercício 03 - PG 62

# Prepare um algoritmo capaz de inverter um número, de 3 dígitos, fornecido, ou seja,
# apresentar primeiro a unidade e, depois, a dezena e a centena.

numero = int(input("Digite um numero de 3 digitos: "));
numeroInvertido = int(str(numero)[::-1]);

print(f'O numero invertido é: {numeroInvertido}')