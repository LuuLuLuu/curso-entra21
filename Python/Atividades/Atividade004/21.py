"""
22. Faça um programa que leia a altura e o sexo (M ou F) de uma pessoa e calcule o peso ideal. 
Para homens, o peso ideal é calculado pela fórmula: (72.7 * altura) - 58. Para mulheres, o peso 
ideal é calculado pela fórmula: (62.1 * altura) - 44.7.
"""


altura = float(input("Informe sua altura: "))
genero = input("Informe seu gênero (M / F): ").upper()

if genero == 1:
    print(f"Seu peso ideal é de {altura*72.7-58}")
elif genero == "F":
    print("")
