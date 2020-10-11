# Exercicio 12 PG-63
# Construa um algoritmo que seja capaz de concluir qual dentre os seguintes animais foi escolhido, através de
# perguntas e respostas. Animais possíveis: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, águia
# tartaruga, crocodilo e cobra


mamifero = input("É mamifero?: ")

if mamifero == "sim":
    print("mamimero")
elif mamifero == "nao":
    aves = print("É ave?: ")

    if aves == "sim":
        print("Aves")
    elif aves == "nao":
        print("Nao a")