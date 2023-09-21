"""
21. Faça um programa que leia a idade de uma pessoa e exiba se ela é criança (até 12 anos), 
adolescente (13 a 17 anos), adulto (18 a 59 anos) ou idoso (maiores de 60 anos).
"""

idade = int(input("Informe a sua idade: "))

if idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <=59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")