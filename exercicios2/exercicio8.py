# Exercicio 14 PG-64

numero1 = int(input('Digite o numero 1 '))
numero2 =   int(input('Digite o numero 2 '))

def mdc(a,b):
    if a< b:
        return mdc(b,a)
    if b==0:
        return a
    r = a % b
    return mdc(b,r)

print(mdc(numero1, numero2))
