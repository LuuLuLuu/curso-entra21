"""
4. Escreva um programa que solicite ao usuário uma sequência de números inteiros positivos
até que o usuário digite um número menor ou igual a 0. Ao final, o programa deve mostrar a
soma dos números lidos.
"""

acumulador = 0

i = 0
while True:
    num = int(input("Digite um número inteiro positivo para ser somado com o próximo: "))
    i += 1

    if num <= 0:
        break

    acumulador += num

print(f"A soma dos números lidos é {acumulador}.")
