# Exercicio 12 PG-63

mamifero = input("É mamifero?: ")
if mamifero == "sim":
    quadrupede = input("É quadrupede?: ")
    if quadrupede == "sim":
        carnivoros = input("É carnivoro?: ")
        if carnivoros == "sim":
            print("Leão")
        else:
            print("Cavalo")
    elif quadrupede == "nao":
        bipedes = input("É bipedes?: ")
        if bipedes == "sim":
            onivoro = input("É ónivoro?: ")
            if onivoro == "sim":
                print("Homem")
            else:
                print("Macaco")
        elif bipedes == "nao":
            voadores = input("É voadores?: ")
            if voadores == "sim":
                print("Morcego")
            else:
                print("Baleia")
elif mamifero == "nao":
    aves = input("É aves?: ")
    if aves == "sim":
        nao_voadoras = input("É não-voadora?: ")
        if nao_voadoras == "sim":
            tropicais = input("É tropical?: ")
            if tropicais == "sim":
                print("Avestruz")
            else:
                print("Pinguim")
        elif nao_voadoras == "nao":
            nadadoras = input("É nadadora?: ")
            if nadadoras == "sim":
                print("Pato")
            else:
                print("Águia")
    if aves == "nao":
        com_casco = input("Possui casco?: ")
        if com_casco == "sim":
            print("Tartaruga")
        elif com_casco == "nao":
            carnivoros = input("É carnivoro?: ")
            if carnivoros == "sim":
                print("Crocodilo")
            else:
                print("Cobra")


