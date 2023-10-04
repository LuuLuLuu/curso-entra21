"""
7. Escreva um programa que receba uma lista de números e retorne apenas os números 
que são únicos, ou seja, sem duplicatas.
"""

entrada = input("Digite uma lista de números separados por espaços: ")

numeros = [int(numero) for numero in entrada.split()]

conjunto = set(numeros)

print(conjunto)
