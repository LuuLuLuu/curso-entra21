"""
16. Crie um algoritmo que solicite ao usuário um número e mostre todos os divisores desse número.
"""

x = int(input("Digite um número: "))
y = x

while True:
    if x % y == 0:
        print(f"{x} é divisível por {y}")
    y -= 1
    if y == 0:
        break
