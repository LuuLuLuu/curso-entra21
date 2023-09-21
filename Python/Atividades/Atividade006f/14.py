"""
14. Escreva um programa que calcule e mostre o valor de x elevado a n. O programa deverá fazer o 
cálculo da potenciação utilizando laços de repetição (Não usar o operador de exponenciação).
"""

num = int(input("Digite o número:"))
exp = int(input("Digite o expoente:"))
x = 1

for i in range(exp):
    x *= num

print(x)
