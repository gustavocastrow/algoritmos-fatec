def epar(x):
    return x % 2 == 0

# Funcao Fatorial

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
