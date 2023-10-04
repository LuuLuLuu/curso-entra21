"""
13. Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é 
Equilátero, Isósceles ou Escaleno. 

Sendo que:
Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isósceles: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes.
"""

base = float(input("De a medida da base do triângulo: "))
lado1 = float(input("De a medida de um dos lados do triângulo: "))
lado2 = float(input("De a medida do outro lado do triângulo: "))

if base == lado1 == lado2:
    print("Este é um triângulo equilátero!")
elif base == lado1 != lado2 or base == lado2 != lado1 or lado1 == lado2 != base:
    print("Este é um triângulo isósceles!")
else:
    print("Este é um triângulo escaleno!")
