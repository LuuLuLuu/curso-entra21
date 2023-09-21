"""
18. Construa um algoritmo que leia o preço de um produto, o percentual de desconto e
calcule o valor a pagar e o valor do desconto.
"""

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a quantidade de desconto: ")) / 100

valor_desconto = preco * desconto
valor_pagar = preco - valor_desconto

print(f"Com o desconto de R${valor_desconto:.2f} o preço do produto será de R${valor_pagar:.2f}.")
