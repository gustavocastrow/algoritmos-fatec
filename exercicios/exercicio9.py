# Exercicio 2.6 PG 46-47

# Escreva um algoritmo que leia o código de um determinado produto e mostre a sua classificação. Utilize a seguinte
# tabela como referências:

codigo_digitado = int(input("Informe um codigo de 1 a 15: "))

if codigo_digitado == 1:
    print(f'O codigo informado {codigo_digitado} é referente a: ALIMENTO NAO-PERECIVEL')
elif codigo_digitado == 2 or codigo_digitado == 3 or codigo_digitado == 4:
    print(f'O codigo informado {codigo_digitado} e referente a: ALIMENTO PERECIVEL ')
elif codigo_digitado == 5 or codigo_digitado == 6:
    print(f'O codigo informado {codigo_digitado} e referente a: VESTUARIO')
elif codigo_digitado == 7:
    print(f'O codigo informado {codigo_digitado} e referente a: HIGIENE PESSOAL')
elif codigo_digitado >= 8 and codigo_digitado <= 15:
    print(f'O codigo informado {codigo_digitado} e referente a: LIMPEZA DE UTENSILIOS DOMESTICOS')
elif codigo_digitado > 15:
    print(f'Codigo {codigo_digitado} invalido, favor informar um codigo entre 1 - 15')