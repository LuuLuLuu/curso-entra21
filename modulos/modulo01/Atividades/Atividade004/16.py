"""
17. Faça um algoritmo que leia um número (deve possuir 3 dígitos) e, se ele for positivo, 
mostre na tela o número em ordem inversa; caso contrário, mostre o valor absoluto do número.
"""


n = int(input("Digite um número diferente de zero: "))

if n > 0:
    print(f"O inverso de {n} é {1/n}")
else:
    print(f"O valor absoluto do número é {-1*n}")
