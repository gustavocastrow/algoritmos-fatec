for c in range(0, 6):
    print('Oi')


n = int(input("Informe um numero: "))

for numero in range(0, n+1):
    print(numero)

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

for x in range(inicio, fim+1, passo):
    print(x)
