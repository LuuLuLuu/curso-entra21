"""
6. Escreva uma expressão lambda que recebe um número como entrada e retorna o quadrado
desse número.
"""

x = int(input("Digite um número inteiro: "))

quadrado = lambda num: num ** 2

print(f"O quadrado de {x} é {quadrado(x)}")
