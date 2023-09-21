"""
20. Faça um programa que leia três números e exiba se eles formam um triângulo válido. 
Um triângulo é válido se a soma de dois lados for maior que o terceiro lado.
"""

l1 = float(input("Informe o tamanho do lado 1 do triângulo: "))
l2 = float(input("Informe o tamanho do lado 2 do triângulo: "))
l3 = float(input("Informe o tamanho do lado 3 do triângulo: "))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print("É um triângulo válido.")
else:
    print("O triângulo é inválido.")
    