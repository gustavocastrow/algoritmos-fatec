# Usando WHILE

x = 1
while x <= 3:
    print(x)
    x = x + 1

fim = int(input("Digite o ultimo numero: "))
x = 0
while x <= fim:
    if x % 2 == 0:
        print (x)
    x = x + 1

tabuada = 1

while tabuada <= 10:
    n = 1
    print("Tabuada %d" %tabuada)
    while n <= 10:
        print("%d x %d = %d" %(tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1

# %d -> int
# %s -> string
# %f -> float

