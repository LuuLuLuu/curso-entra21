"""
19. Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de
vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de
comissão sobre suas vendas efetuadas, informar o total a receber no final do mês,
com duas casas decimais.
"""

nome = input("Digite o nome do vendedor: ")
salario = float(input("Digite o salário: "))
vendas = float(input("Digite a quantidade de vendas(em dinheiro): "))
COMISSAO = 0.15
receber = COMISSAO * vendas + salario

print(f"Junto do salário e da comissão, {nome} tem a receber R${receber:.2f}.")
