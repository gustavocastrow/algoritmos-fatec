#Em um prédio há três elevadores denominados A, B e C. Para otimizar o sistema de controle dos elevadores foi realizado
# um levantamento no qual cada usuário respondia:
# • o elevador que utilizava com mais frequência:
# • o período em que utilizava
# o elevador, entre • 'M' = matutino; • 'V' = vespertino; • 'N' = noturno. Construa um algoritmo que calcule e imprima:
# • qual é o elevador mais freqüentado e em que período se concentra o maior fluxo:
# • qual o período mais usado de todos e a que elevador pertence:
# • qual a diferença porcentual entre o mais usado dos horários e o menos usado;
# • qual a porcentagem sobre o total de serviços prestados do elevador de média utilização.

elevadorAmatutino = elevadorAvespertino  = elevadorAnoturno = 0
elevadorBmatutino = elevadorBvespertino  = elevadorBnoturno = 0
elevadorCmatutino = elevadorCvespertino  = elevadorCnoturno = 0
elevador = str
while elevador != 1:
    elevador = input('DIGITE QUAL ELEVADOR VOCÊ MAIS USA A - B - C \n ou [1] para sair ').upper()
    if elevador =='1':
       break;
    periodo = input('DIGITE QUAL PERIODO VOCÊ MAIS USA [M]atutino [V]espertino [N]oturno ').upper()
    if elevador =='A' :
        if periodo =='M':
            elevadorAmatutino += 1;
        elif periodo =='V':
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
# • o elevador que utilizava com mais frequência:
elevadorAtotal =   (elevadorAmatutino+elevadorAvespertino+elevadorAnoturno)
elevadorBtotal = (elevadorBmatutino+elevadorBvespertino+elevadorBnoturno)
elevadorCtotal = (elevadorCmatutino+elevadorCvespertino+elevadorCnoturno)
if elevadorAtotal > elevadorCtotal and elevadorAtotal > elevadorBtotal:
    print(f' o elevador que mais foi utilizado foi o ELEVADOR A  com {elevadorAtotal} total de pessoas usando')
elif elevadorBtotal > elevadorAtotal and elevadorBtotal > elevadorCtotal:
    print(f' o elevador que mais foi utilizado foi o ELEVADOR B  com {elevadorBtotal} total de pessoas usando')
else:
    print(f' o elevador que mais foi utilizado foi o ELEVADOR C  com {elevadorCtotal} total de pessoas usando')
# • o período em que utilizava
periodoTotalMatutino =  elevadorBmatutino + elevadorAmatutino + elevadorCmatutino
periodoTotalVerpertino = elevadorAvespertino + elevadorBvespertino + elevadorCnoturno
periodoTotalNoturno = elevadorAnoturno + elevadorBnoturno + elevadorCnoturno
if periodoTotalMatutino > periodoTotalVerpertino and periodoTotalMatutino > periodoTotalNoturno:
    print (f'O periodo mais usado nos elevadores foi o  Matutino , com {periodoTotalMatutino} pessoas')
elif periodoTotalVerpertino > periodoTotalMatutino and periodoTotalVerpertino > periodoTotalNoturno:
    print (f'O periodo mais usado nos elevadores foi o  Matutino , com {periodoTotalVerpertino} pessoas')
else:
    print(f'O periodo mais usado nos elevadores foi o  Matutino , com {periodoTotalNoturno} pessoas')

# • qual a diferença porcentual entre o mais usado dos horários e o menos usado;
# • qual a porcentagem sobre o total de serviços prestados do elevador de média utilização.
