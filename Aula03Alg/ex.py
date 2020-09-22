# EX08

qtd_km = int(input("Informe a quantidade de km percorridos: "))
qtd_dias = int(input("Informe a quantidade de dias: "))

custo_alguel_carro = qtd_dias * 60.00
custo_km_percorrida = qtd_km * 0.15

custo_final = custo_alguel_carro + custo_km_percorrida

print("O custo total é de %.2f" %custo_final)