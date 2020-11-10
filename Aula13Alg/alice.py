file_alice = open("alice.txt")

def analisar_palavras(palavra, dict_resultado):
    for palavra in palavras:
        if len(palavra) > 3: #Se o tamanho da palavra
            if palavra in dict_resultado.keys(): #Verifica se a palavra existe dentro do dicionario
                dict_resultado[palavra] +=1 #Pega o valor referente ao valor, e encrementa e atribiu novamente a chave dentro do resultado
            else:
                dict_resultado[palavra] = 1 #Caso nao exista dentro da estrtura ela ira inicalizar

dict_resultado = {}

for linha in file_alice.readlines():
    palavras = linha.strip().split(' ')
    analisar_palavras(palavras, dict_resultado)
print(dict_resultado)
