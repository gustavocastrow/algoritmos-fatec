nome = input("Informe o nome do produto: ")
grupo = input("Grupos: A | B | O (Outros): ")
preco_fabrica = float(input("Informe o preco de fabrica: "))

margem_lucro = 0.0

if grupo.lower() == 'a':
    margem_lucro = 1.2
elif grupo.lower() == 'b':
    margem_lucro = 1.3
else:
    margem_lucro = 1.1

# print("Nome: {} - Grupo: {} - Preço de Fabrica: {:.2f} - Preco de Venda: {:.2f}".format(nome, grupo.upper(), (preco_fabrica * margem_lucro)))
print(f"{nome}, {grupo}, preco de fabrica R$: {preco_fabrica} preco de venda: R${preco_fabrica * margem_lucro}")