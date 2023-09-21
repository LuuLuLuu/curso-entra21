"""
5. Crie um algoritmo que mostre os números de 1 a 100 e ao final mostre a soma de todos eles.
"""

acumulador = 0
for i in range(1, 101):
    print(f"{i}")
    acumulador += i

print(f"A soma entre todos estes números é {acumulador}")
