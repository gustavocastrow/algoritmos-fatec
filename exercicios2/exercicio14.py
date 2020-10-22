# Exercicio 20 PG-64
# Uma rainha requisitou os serviçõs de um monge e disse-lhe que pagaria qualquer preço. O monge, necesitando de
# alimentos, perguntou a rainha se o pagamento poderia ser feito com grãos de trigo dispostos em um tabuleiro de xadrez
# de tal forma que o primeiro quadro contivesse apenas grão e os quadros subsquentes, o dobro do quadro anterior
# A rainha considerou o pagamento barato e pediu que o serviço fosse executado, sem se dar conta de que seria impossivel
# efetuar o pagamento. Faça um algoritmo para calcular o numero de grãos que o monge deve receber.


# 64 quadros
# 1quadro = 1 grão -> 2quadro = 2 grao -> 3 quadro = 4

quadro = 1

for grao in range(0, 65):
    quadro = quadro * 2
print(f'A quantidade de grãos é: {quadro}')