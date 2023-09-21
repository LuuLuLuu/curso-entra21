"""
10. Escreva um programa que receba uma lista de palavras e retorne a palavra mais longa.
"""

entrada = input("Digite uma lista de palavras separadas por espaços: ")
palavras = entrada.split()
palavra_mais_longa = ""

for palavra in palavras:
    if len(palavra) > len(palavra_mais_longa):
        palavra_mais_longa = palavra

if palavra_mais_longa:
    print(f"A palavra mais longa é: {palavra_mais_longa}")
else:
    print("Nenhuma palavra foi fornecida.")