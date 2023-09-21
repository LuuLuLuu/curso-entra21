"""
12. Escreva um programa que calcule o produto da multiplicação de dois fatores. 
O programa deve realizar os cálculos utilizando laços de repetição e adição.
"""

x1 = int(input("Digite um número: "))
x2 = int(input("Digite outro número: "))

produto = 0

if x1 != 0 and x2 != 0:
    if x1 < 0:
        x1 = -x1
        x2 = -x2

    for i in range(x1):
        produto += x2

    print(f"Produto = {produto}")
else:
    print("Produto = 0")
