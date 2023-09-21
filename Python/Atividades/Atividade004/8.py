"""
8. Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) 
e informe se o resultado foi um empate, a vitória do primeiro time ou do segundo time.
"""

time1 = int(input("Digite os pontos do time 1: "))
time2 = int(input("Digite os pontos do time 2: "))

vitoria = True

if time1 > time2:
    print(f"O time 1 ganhou.")
elif time1 < time2:
    print(f"O time 2 ganhou.")
else:
    input("Houve um empate.")

