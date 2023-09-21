"""
21. Escreva um programa que calcule o valor futuro de um investimento com base
no montante inicial, na taxa de juros e no período de tempo. Peça ao usuário para
inserir essas informações e exiba o valor futuro. Você pode utilizar a fórmula de
juros compostos para realizar o cálculo.
"""

montante_inicial = float(input("Digite o montante inicial: "))
juros = float(input("Digite a quantidade de juros: ")) / 100
tempo = float(input("Digite o período de tempo: "))

calculo = montante_inicial * (1+juros)**tempo

print(f'Ao final de {tempo:.0f} meses, ao juros de {juros}%, você terá acumulado um total de: R${calculo:.2f}.')
