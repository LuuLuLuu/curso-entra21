"""
18. Crie um algoritmo que receba uma palavra e informe se ela é ou não um palíndromo. 
"""

palavra = input("Digite uma palavra: ")
palavra_invertida = ""

for letra in palavra:
    palavra_invertida = letra + palavra_invertida

if palavra == palavra_invertida:
    print(f"{palavra} é um palíndromo!")
else:
    print(f"{palavra} não é um palíndromo.")
    