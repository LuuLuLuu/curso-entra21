"""
7. Escreva um programa que solicite ao usuário um número inteiro positivo e exiba a soma dos dígitos desse número.
"""

numero = input("Digite um número: ")
soma = 0

for digito in numero:           # Aqui não é nescessário o range, pois a quantidade que será percorrida é
    soma += int(digito)         # correspondente a largura da string. O digito recebe o elemento da posição
                                # correspondente ao laço no qual está.

print(f"A soma dos digitos deste número é: {soma}")
