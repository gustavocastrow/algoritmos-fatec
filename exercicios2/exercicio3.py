# Exercicio 9 PG-63

dia = int(input("Informe o dia de nascimento: "))
mes = int(input("Informe o mes de nascimento: "))

# Áries: de 21 Março(3) a 20 Abril(4)
if dia >= 21 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 20 and  mes == 4:
   print("Aries")
# Touro: 21 Abril(4) a 20 Maio(5)
elif dia >= 21 and dia <= 30 and mes == 4 or dia >= 1 and dia <= 20 and mes == 5:
    print("Touro")
# Gêmeos: 21 Maio(5) a 20 Junho(6)
elif dia >= 21 and dia <= 31 and mes == 5 or dia >= 1 and dia <= 20 and mes == 6:
    print("Gêmeos")
# Câncer: 21 Junho(6) a 22 Julho(7)
elif dia >= 21 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 20 and mes == 7:
    print("Câncer")
# Leão: 23 Julho(7) a 22 Agosto(8)
elif dia >= 23 and dia <= 31 and mes == 7 or dia >= 1 and dia <= 22 and mes == 8:
    print("Leão")
# Virgem: 23 Agosto(8) a 22 Setembro (9)
elif dia >= 23 and dia <= 31 and mes == 8 or dia >= 1 and dia <= 22 and mes == 9:
    print("Virgem")
# Libra:  23 Setembro(9) a 22 Outubro(10)
elif dia >= 23 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 22 and mes == 10:
    print("Libra")
# Escorpião: 23 outubro(10) a 21 novembro(11)
elif dia >= 23 and dia <= 31 and mes == 10 or dia >= 1 and dia <= 21 and mes == 11:
    print("Escorpião")
# Sagitário: 22 novembro(11) a 21 dezembro(12)
elif dia >= 21 and dia <= 30 and mes == 11 or dia >= 1 and dia <= 21 and mes == 12:
    print("Sagitário")
# Capricórnio: 22 dezembro(12) a 20 janeiro(1)
elif dia >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 20 and mes == 1:
    print("Capricórnio")
# Aquário: 21 janeiro(1) a 18 fevereiro(2)
elif dia >= 21 and dia <= 31 and mes == 1 or dia >= 1 and dia <= 18 and mes == 2:
    print("Aquário")
# Peixes: 19 fevereiro(2) a 20 março(3)
elif dia >= 19 and dia <= 29 and mes == 2 or dia >=1 and dia <= 20 and mes == 3:
    print("Peixes")
else:
    print("Insira uma data válida")






