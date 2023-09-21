"""
3. Escreva um programa que solicite ao usuário um número inteiro positivo e exiba a
tabuada desse número de 1 a 10 utilizando um loop for.
"""

num = int(input("Digite um número inteiro e positivo: "))

# Tabuada
i = 0
while i < 11:
    print(f"{i} x {num} = {i*num}")
    i += 1
