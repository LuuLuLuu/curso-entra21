"""
5. Escreva um programa que solicite um número e informe se ele é divisível por 5.
"""

x = input("Digite um número: ")

if x[-1] == ".5":
    exit()

if x[-1] == "0" or x[-1] == "5":
    print(f"O número {x} é divisível por 5.")
