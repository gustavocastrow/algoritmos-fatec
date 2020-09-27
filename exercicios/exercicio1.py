# Exercício 01 - PG 62

# Construa um algoritmo que calcule a média ponderada entre 5 números quaisquer, sendo que os pesos a serem aplicados
# são 1, 2, 3, 4 e 5 respectivamente.


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))

media = int((n1 * 1) + (n2 * 2) + (n3 * 3) + (n4 * 4) + (n5 * 5)) / (n1+n2+n3+n4+n5)
input(f'A média ponderada dos cinco números é: {media:.2f}')