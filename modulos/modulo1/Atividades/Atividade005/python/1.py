"""
1. Escreva um programa que pergunte a quantidade de km percorridos por um carro 
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e 
R$ 0,15 por km rodado.
"""


carro = {
    "km": int(input("Informe a quantidade de Km percorridos pelo seu carro: ")),
    "dias": int(input("Informe a quantidade de dias em que seu carro foi alugado: "))
}

calculo = carro["km"] * 0.15 + 60 * carro["dias"];

print(f"O custo total será de R${calculo:.2f}.")
