"""
2. Escreva um programa que receba um número, se esse número for par, mostre na
tela a metade do número digitado. No final do programa mostre na tela a mensagem:
 “Programa finalizado…”.
"""

x = int(input("Digite um número: "))
par = x % 2

if not par:
    print(x/2)
    print("Programa finalizado…")
