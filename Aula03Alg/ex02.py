# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

print('----Calculo de Tempo em Segundos----')
n1=int(input('Quantos Dias: '))
n2=int(input('Quantas Horas: '))
n3=int(input('Quantos minutos: '))

segs=(n3*60)+(n2*3600)+(n1*86400)
print(segs)

print('Calculo de tempo em segundos')
