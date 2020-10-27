## Exercicio 35 PG-67

elevadorAmatutino = elevadorAvespertino  = elevadorAnoturno = 0
elevadorBmatutino = elevadorBvespertino  = elevadorBnoturno = 0
elevadorCmatutino = elevadorCvespertino  = elevadorCnoturno = 0
elevador = str
while elevador != 1:
    elevador = input('Informe qual elevador você mais usa: A - B - C \n ou [1] para sair ').upper()
    if elevador == '1':
       break;
    periodo = input('Informe qual periodo você mais usa: [M]atutino [V]espertino [N]oturno ').upper()
    if elevador == 'A':
        if periodo == 'M':
            elevadorAmatutino += 1;
        elif periodo == 'V':
            elevadorAvespertino += 1;
        elif periodo == 'N':
            elevadorAnoturno += 1;
        else:
            print('OPÇÃO INVALIDA')

    if elevador == 'B':
        if periodo == 'M':
            elevadorBmatutino += 1;
        elif periodo == 'V':
            elevadorBvespertino += 1;
        elif periodo == 'N':
            elevadorBnoturno += 1;
        else:
            print('OPÇÃO INVALIDA')
    if elevador == 'C':
        if periodo == 'M':
            elevadorCmatutino += 1;
        elif periodo == 'V':
            elevadorCvespertino += 1;
        elif periodo == 'N':
            elevadorCnoturno += 1;
        else:
            print('OPÇÃO INVALIDA')

elevadorAtotal = (elevadorAmatutino+elevadorAvespertino+elevadorAnoturno)
elevadorBtotal = (elevadorBmatutino+elevadorBvespertino+elevadorBnoturno)
elevadorCtotal = (elevadorCmatutino+elevadorCvespertino+elevadorCnoturno)

if elevadorAtotal > elevadorCtotal and elevadorAtotal > elevadorBtotal:
    print(f' o elevador que mais foi utilizado foi o ELEVADOR A  com {elevadorAtotal} total de pessoas usando')
elif elevadorBtotal > elevadorAtotal and elevadorBtotal > elevadorCtotal:
    print(f' o elevador que mais foi utilizado foi o ELEVADOR B  com {elevadorBtotal} total de pessoas usando')
else:
    print(f' o elevador que mais foi utilizado foi o ELEVADOR C  com {elevadorCtotal} total de pessoas usando')

periodoTotalMatutino =  elevadorBmatutino + elevadorAmatutino + elevadorCmatutino
periodoTotalVerpertino = elevadorAvespertino + elevadorBvespertino + elevadorCnoturno
periodoTotalNoturno = elevadorAnoturno + elevadorBnoturno + elevadorCnoturno

if periodoTotalMatutino > periodoTotalVerpertino and periodoTotalMatutino > periodoTotalNoturno:
    print (f'O periodo mais usado nos elevadores foi o  Matutino , com {periodoTotalMatutino} pessoas')
elif periodoTotalVerpertino > periodoTotalMatutino and periodoTotalVerpertino > periodoTotalNoturno:
    print (f'O periodo mais usado nos elevadores foi o  Matutino , com {periodoTotalVerpertino} pessoas')
else:
    print(f'O periodo mais usado nos elevadores foi o  Matutino , com {periodoTotalNoturno} pessoas')
