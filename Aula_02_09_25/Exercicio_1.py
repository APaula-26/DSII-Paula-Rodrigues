# Desenvolva um programa que recebe do usuário, o placar de um jogo de futebol (os gols de cada time) e informa se o resultado
# foi um empate, se a vitória foi do primeiro time ou do segundo time

T1 = int(input("Informe quantos gols o primeiro time fez: "))
T2 = int(input("Informe quantos gols o segundo time fez: "))

if T1 == T2:
    print("Empate!!")
elif T2 > T1:
    print("Vitória do time 2!!")
else: 
    print("Vitória do time 1!!")