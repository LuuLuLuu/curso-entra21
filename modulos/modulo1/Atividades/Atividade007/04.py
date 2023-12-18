"""
4. Escreva um programa que receba duas listas e retorne uma nova lista que contenha
apenas os elementos em comum entre as duas listas.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

elementos_em_comum = [elemento for elemento in lista1 if elemento in lista2]

print("Elementos em comum entre as duas listas:", elementos_em_comum)
