media_aritmetica = 78.5
media_pondera = 80.5

notas_turma = [56.7, 87.9, 100.0, 45.7]
nota = 0.0
for nota in notas_turma:
    if nota >= media_aritmetica:
        print(nota)

print(nota)


# Faça um programa que leia uma palavra e troque as vogais por ''*'' usando for

palavra = input("Palavra: ")
troca = ""
for letra in palavra:
    if letra in "aeiou":
        troca = troca + "*"
    else:
        troca = troca + letra
print(f"Nova palavra {troca}")