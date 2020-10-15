# Podemos associar o terreo ao andar zero, e o primeiro é o andar 1 e assim por diante


# Primeira dimensão [] -> linhas, eixo X
# Segunda dimensão [[colunas, eixo Y]]

matriz3x3 = [[3, 4, 5, ], #linha1 (0)
    [6, 7, 8, ], #linha2 (1)
    [11, 45, 67] #linha3 (2)
]

print(matriz3x3[0]) # [3,4,5]
print(matriz3x3[1][1]) #7
print(matriz3x3[2][2]) #67

matriz3x3[0] = [78, 345, 90]
matriz3x3[1][1] = 657
# =======================================================================================

edificio = ["Familia Souza", "Familia Brito", "Sr Jorge", "Familia Tanaka"]
print(edificio[0])
print(edificio[1])
print(edificio[2])
print(edificio[3])

for familia in edificio:
    print(familia)

# =========================================================================================

# Adicionando elementos no array.
# lista.append("nome do elemento")

lista = ["Elemento 01", "Elemento 02", "Elemento 03"]
lista.append("Elemento novo")
lista.append(89)
lista.append(True)
lista.append(98.2)
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])

# Acessando ultimo elemento do array
print(edificio[len(edificio) -1])

# Concatenando arrays

edificio = edificio + lista
print(edificio)

# Removendo um elemento do array

del edificio[1] #Removendo a FAMILIA BRITO
print(edificio)

# Fatiando elementos do array

var2 = edificio[0:3]
print(var2)

# Verificar se dentro de edicifio existe o número 89
if 89 in edificio:
    print("O valor existe")

# lista.extende(lista) concatena com outra lista
# lista.count(elemento)
# lista.index(elemento) retorna o indice do elemento
# lista.insert(n, dado) adicona o elemento no N(numero) do index passado
# elementoRemovido = lista.pop(indice) remove o elemento do array e retorna
# lista.remove(index) remove sem retornar
