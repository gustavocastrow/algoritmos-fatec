# Exercicio 29 PG-64
#
from random import  random

empresa1 = int(input('Digite o numero de funcionarios da Empresa 1 '))
empresa2 = int(input('Digite o numero de funcionarios da Empresa 2 '))
empresa3 = int(input('Digite o numero de funcionarios  da Empresa 3 '))


print(f' EMPRESA 1 {empresa1} FUNCIONARIOS \n  EMPRESA 2 {empresa2} FUNCIONARIOS \n ')

if empresa1 >= 400:
    print(f' EMPRESA 1 {empresa1} funcionarios --Grande porte')
elif empresa1 < 400:
    print(f' EMPRESA 1 {empresa1}  funcionarios --Medio porte')
else:
    print(f' EMPRESA 1 {empresa1} funcionarios -- Pequeno porte')

if empresa2 >= 400:
    print(f' EMPRESA 2  {empresa2} funcionarios --grande porte')
elif empresa2 < 400:
    print(f' EMPRESA 2  {empresa2} funcionarios --MEDIO porte')
else:
    print(f' EMPRESA 2  {empresa2} funcionarios --PEQUENO porte')
if empresa3 >= 400:
    print(f' EMPRESA 3  {empresa3} funcionarios --grande porte')
elif empresa3 < 400:
    print(f' EMPRESA 3  {empresa3} funcionarios --MEDIO porte')
else:
    print(f' EMPRESA 3  {empresa3} funcionarios --PEQUENO porte')
