"""
12. Escreva um programa que receba três valores: A, B e C. Faça as comparações necessárias 
para exibir na tela o maior valor entre os três.
"""

a = int(input("Digite um número"))
b = int(input("Digite outro número"))
c = int(input("Digite outro número"))

maximo = max(a, b, c)

print(f"O maior valor dentre os três números dados é o {maximo}")
