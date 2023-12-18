"""
11. Faça um programa que receba uma lista de números inteiros e retorne uma nova lista com os 
elementos em ordem crescente.
"""

entrada = input("Digite uma lista de números inteiros separados por espaços: ")
numeros = [int(numero) for numero in entrada.split()]
numeros_ordenados = sorted(numeros)

print("Números em ordem crescente:", numeros_ordenados)
