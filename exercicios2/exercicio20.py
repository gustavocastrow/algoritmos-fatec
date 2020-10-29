# Exercicio 26 PG-65

s = 1
flag = True

for i in range (2, 11):
    s = s - i/(i**2) if flag else s + i/(i**2)

    flag = not flag
print(f'Resultao de S : {s}')