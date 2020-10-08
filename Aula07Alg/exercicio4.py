# Ex 04 - Aula06
qtde_sup50_pesoinf60 = 0
qtde_pessoas = 3
qtde_pes_altinf_150cm = 0
soma_alt_pes_altinf_150cm = 0.0

qtde_pes_olhos_azuis = 0
qtde_pes_ruivas_sem_olhos_azuis = 0

nr_pessoas_lidas = 0

while nr_pessoas_lidas < qtde_pessoas:
    idade = int(input("Informe sua idade: "))
    peso = float(input("Informe seu peso: "))
    altura = float(input("Informe sua altura: "))
    cor_olhos = input("Informe a cor dos seus olhos: (A-AZUL, P-PRETO, V-VERDE, C-CASTANHO").lower()
    cor_cabelos = input("Informe a cor dos seus cabelos: (P-PRETO, C-CASTANHO, L-LOURO, R-RUIVO").lower()

    # A

    if idade > 50 and peso < 60:
        qtde_sup50_pesoinf60 += 1

    # B
    if altura < 1.5:
        qtde_pes_altinf_150cm += 1
        soma_alt_pes_altinf_150cm += altura


    # C
    if cor_olhos == 'a':
        qtde_pes_olhos_azuis += 1


    # D
    if cor_cabelos == 'r' and cor_olhos != 'a':
        qtde_pes_ruivas_sem_olhos_azuis += 1

        nr_pessoas_lidas += 1


print(f'A quantidade de pessoas com idade superior a 50 e peso inferior a 60 quilos é {qtde_sup50_pesoinf60}')
print(f'A media das idades das pessoas com altura inferior a 1,50m é {(soma_alt_pes_altinf_150cm / qtde_pes_altinf_150cm)} ')
print(f'A porcentagem de pessoas com olhos azuis entre todas as analisadas e de {qtde_pes_olhos_azuis / qtde_pessoas}')
print(f'A quantidade de pessoas ruivas sem olhos azuis e {qtde_pes_ruivas_sem_olhos_azuis}')