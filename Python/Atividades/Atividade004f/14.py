"""
15. Para doar sangue é necessário ter entre 18 e 67 anos. Faça um programa que pergunte a idade
 de uma pessoa e diga se ela pode doar sangue ou não. Para realizar essa questão utilize o 
 operador lógico OU.
"""

idade = int(input("Informe a sua idade: "))

if idade < 18 or idade > 67:
    print("Tu não pode realizar a doação de sangue.")
else:
    print("Tu pode realizar a doação de sangue.")
