def read_file(file_telefone):
    content_file = file_telefone.read() #Lendo todos os conteudos existentes no arquivo
    content_file = content_file.replace('\n', ' ')
    content_file = content_file.strip()
    lst_telefone = content_file.split(' ')
    return lst_telefone

#Nao pode haver dois digitos consecutivos identicos

def has_digitos_consecutivos(telefone):
    digito1 = telefone[0]
    for digito2 in telefone[1:]:
        if digito1 == digito2:
            return True
        else:
            digito1 = digito2
    return False

def soma_e_par(telefone):
    soma = 0
    for digito in telefone:
        soma += int(digito)
    return (soma % 2) == 0

def primeiro_igual_ultimo(telefone):
    return telefone[0] == telefone[-1]




file_telefone = open('telefones.txt') #Especificando o arquivo que sera aberto/lido (entrada)
file_tel_validos = open('tel_validos.out', 'w', encoding='utf-8')
file_tel_invalidos = open('tel_invalidos.out', 'w', encoding='utf-8')

total_telefones_analisados = 0
total_telefones_validos = 0

for telefone in read_file(file_telefone):
    total_telefones_analisados += 1
    if not has_digitos_consecutivos(telefone) \
        and soma_e_par(telefone) \
        and not primeiro_igual_ultimo(telefone):
        total_telefones_validos += 1
        file_tel_validos.write("{}{}".format(telefone, '\n'))
        # Salvar em telefones validos
    else:
        file_tel_invalidos.write("{}{}".format(telefone, '\n'))
        # Salvar em telefones invalidos
file_tel_validos.write(f'{total_telefones_analisados} | {total_telefones_validos}')

#Fechando o arquivo para nao usar mais.
file_telefone.close()
file_tel_validos.close()
file_tel_invalidos.close()
