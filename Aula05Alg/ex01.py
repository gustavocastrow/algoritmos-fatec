# ler dois valores e imprimir o maior deles

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor:"))

if a > b:
    print("O primeiro numero e o maior")
else:
    if b > a:
        print("O segundo numero e maior")
    else:
        print("Ambos os valores sao iguals")
if b > a:
    print("O segundo numero e o maior")