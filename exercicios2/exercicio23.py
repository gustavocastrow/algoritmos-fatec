# Exercicio 29 PG-65
#
from random import  random

empresa1 = int(input('Digite o numero de funcionarios da Empresa 1:  '))
empresa2 = int(input('Digite o numero de funcionarios da Empresa 2: '))
empresa3 = int(input('Digite o numero de funcionarios  da Empresa 3: '))


print(f' Empresa 01  {empresa1} funcionarios \n  Empresa 02 {empresa2} funcionarios \n ')

if empresa1 >= 400:
    print(f' Empresa 01 {empresa1} funcionarios --> Grande porte')
elif empresa1 < 400:
    print(f' Empresa 01 {empresa1} funcionarios --> Medio porte')
else:
    print(f' Empresa 01 {empresa1} funcionarios --> Pequeno porte')

if empresa2 >= 400:
    print(f' Empresa 02  {empresa2} funcionarios --> grande porte')
elif empresa2 < 400:
    print(f' Empresa 02  {empresa2} funcionarios --> MEDIO porte')
else:
    print(f' Empresa 02  {empresa2} funcionarios --> PEQUENO porte')
if empresa3 >= 400:
    print(f' Empresa 03  {empresa3} funcionarios --> grande porte')
elif empresa3 < 400:
    print(f' Empresa 03  {empresa3} funcionarios --> MEDIO porte')
else:
    print(f' Empresa 03 {empresa3} funcionarios --> PEQUENO porte')
