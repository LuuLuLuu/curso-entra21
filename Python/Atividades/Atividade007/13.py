"""
13. Escreva um programa que receba uma lista como entrada e remova todas as duplicatas, retornando 
uma nova lista com os elementos únicos em sua ordem original.

"""

entrada = input("Digite uma lista de elementos separados por espaços: ")
elementos = entrada.split()
elementos_unicos = []

for elemento in elementos:
    if elemento not in elementos_unicos:
        elementos_unicos.append(elemento)

print("Elementos únicos na ordem original:", elementos_unicos)
