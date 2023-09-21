""""
24. Faça um programae que leia três números  mostre-os em ordem decrescente.
"""

num1 = int(input("Me de o primeiro número: "))      # 6
num2 = int(input("Me de o segundo número: "))       # 3
num3 = int(input("Me de o terceiro número: "))      # 5

# o esperado é 321

if num1 < num2 < num3:
    print(f"{num3} > {num2} > {num1}")
elif num1 < num3 < num2:
    print(f"{num2} > {num3} > {num1}")
elif num2 < num1 < num3:
    print(f"{num3} > {num1} > {num2}")
elif num2 < num3 < num1:
    print(f"{num1} > {num3} > {num2}")
elif num3 < num2 < num1:
    print(f"{num1} > {num2} > {num3}")
elif num3 < num1 < num2:
    print(f"{num2} > {num1} > {num3}")
