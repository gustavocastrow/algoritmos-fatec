# Exercicio 11 PG-63


pais1 = input("Informe o primeiro país: ")
pais1_ouro = int(input(f'Informe a quantidade de OURO do(a) {pais1}: '))
pais1_prata = int(input(f'Informe a quantidade de PRATA do(a) {pais1}: '))
pais1_bronze = int(input(f'Informe a quantidade de BRONZE do(a) {pais1}: '))

pais2 = input("Informe o segundo país: ")
pais2_ouro = int(input(f'Informe a quantidade de OURO do(a) {pais2}: '))
pais2_prata = int(input(f'Informe a quantidade de PRATA do(a) {pais2}: '))
pais2_bronze = int(input(f'Informe a quantidade de BRONZE do(a) {pais2}: '))

pais3 = input("Informe o terceiro país: ")
pais3_ouro = int(input(f'Informe a quantidade de OURO do(a) {pais3}: '))
pais3_prata = int(input(f'Informe a quantidade de PRATA do(a) {pais3}: '))
pais3_bronze = int(input(f'Informe a quantidade de BRONZE do(a) {pais3}: '))

rank_pais1 = (3*pais1_ouro) + (2*pais1_prata) + (1*pais1_bronze)
rank_pais2 = (3*pais2_ouro) + (2*pais2_prata) + (1*pais2_bronze)
rank_pais3 = (3*pais3_ouro) + (2*pais3_prata) + (1*pais3_bronze)

if rank_pais1 > rank_pais2 and rank_pais2 > rank_pais3:
    print(f'1. {pais1} com {pais1_ouro} ouros, {pais1_prata} pratas e {pais1_bronze} bronzes.')
    print(f'2. {pais2} com {pais2_ouro} ouros, {pais2_prata} pratas e {pais2_bronze} bronzes.')
    print(f'3. {pais3} com {pais3_ouro} ouros, {pais3_prata} pratas e {pais3_bronze} bronzes.')
elif rank_pais1 > rank_pais3 and rank_pais3 > rank_pais2:
    print(f'1. {pais1} com {pais1_ouro} ouros, {pais1_prata} pratas e {pais1_bronze} bronzes.')
    print(f'2. {pais3} com {pais3_ouro} ouros, {pais3_prata} pratas e {pais3_bronze} bronzes.')
    print(f'3. {pais2} com {pais2_ouro} ouros, {pais2_prata} pratas e {pais2_bronze} bronzes.')
elif rank_pais2 > rank_pais1 and rank_pais1 > rank_pais3:
    print(f'1. {pais2} com {pais2_ouro} ouros, {pais2_prata} pratas e {pais2_bronze} bronzes.')
    print(f'2. {pais1} com {pais1_ouro} ouros, {pais1_prata} pratas e {pais1_bronze} bronzes.')
    print(f'3. {pais3} com {pais3_ouro} ouros, {pais3_prata} pratas e {pais3_bronze} bronzes.')
elif rank_pais2 > rank_pais3 and rank_pais3 > rank_pais1:
    print(f'1. {pais2} com {pais2_ouro} ouros, {pais2_prata} pratas e {pais2_bronze} bronzes.')
    print(f'2. {pais3} com {pais3_ouro} ouros, {pais3_prata} pratas e {pais3_bronze} bronzes.')
    print(f'3. {pais1} com {pais1_ouro} ouros, {pais1_prata} pratas e {pais1_bronze} bronzes.')
elif rank_pais3 > rank_pais2 and rank_pais2 > rank_pais1:
    print(f'1. {pais3} com {pais3_ouro} ouros, {pais3_prata} pratas e {pais3_bronze} bronzes.')
    print(f'2. {pais2} com {pais2_ouro} ouros, {pais2_prata} pratas e {pais2_bronze} bronzes.')
    print(f'3. {pais1} com {pais1_ouro} ouros, {pais1_prata} pratas e {pais1_bronze} bronzes.')
elif rank_pais3 > rank_pais1 and rank_pais1 > rank_pais2:
    print(f'1. {pais3} com {pais3_ouro} ouros, {pais3_prata} pratas e {pais3_bronze} bronzes.')
    print(f'2. {pais1} com {pais1_ouro} ouros, {pais1_prata} pratas e {pais1_bronze} bronzes.')
    print(f'3. {pais2} com {pais2_ouro} ouros, {pais2_prata} pratas e {pais2_bronze} bronzes.')
else:
    print("Dados inválidos")



