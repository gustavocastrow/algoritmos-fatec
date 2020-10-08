#1. Construa uma função que calcule o arranjo de N elementos,p a  p, utilize a seguinte formula
# A = N!/(N-P)!

def fatorial(n):
    resultado = 1
    if n == 0:
        return 1
    else:
        for valor in range(2, n + 1):
            resultado = resultado * valor
    return resultado


for i in range(5):
    print(fatorial(i))

N = float(input("Informe o valor de N: "))
P = float(input("Informe o valor de P: "))

A = fatorial(N) / fatorial(N - P)

