a = int(input('Digite o primeiro numero'))
b = int(input('Digite o segundo numero'))

def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a,b):
    return abs(a*b) / mdc(a,b)

print("MMC 10 e 5 --> %d" % mmc(a,b))