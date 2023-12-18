"""
4. Escreva um programa que receba um número, se esse número for par, mostre na
 tela “O número é par” senão mostre “O número é ímpar”
"""

x = int(input("Digite um número: "))
par = x % 2

if not par:
    print("O número é par.")
else:
    print("O número é ímpar.")
