# Exercício 04 - PG 62

# Ao completar o tanque de combustível de um automóvel, faça um algoritmo que
# calcule o consumo efetuado, assim como a autonomia que o carro ainda teria antes do abastecimento. Considere que o
# veículo sempre seja abastecido até encher o tanque e que são fornecidas apenas a capacidade do tanque, a quantidade
# de litros abastecidos e a quilometragem percorrida desde o último abastecimento.

autonomia_tanque = int(input("Informe a capacidade total do seu tanque: "))
total_abastecido = int(input("Informe a quantidade de litros abastecidos: "))
km_percorrido = int(input("Informe o número de km percorridos: "))

kmporlitro = km_percorrido / total_abastecido
tanquerestante = autonomia_tanque - total_abastecido
kmrestante =  tanquerestante * kmporlitro


print(f'Total de litros abastecidos: {total_abastecido}')
print(f'O seu veiculo faz {kmporlitro} km por litro')
print(f'O seu veiculo tem uma autonomia de {kmrestante} kms com {tanquerestante} litros')