"""
3. Escreva um programa que pergunte a velocidade do carro de um usuário. 
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi 
multado. Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km 
acima de 80 km/h.
"""

velocidade_carro = int(input("Informe a velocidade do carro em Km/h: "))
km_acima_limite = velocidade_carro - 80
taxa_dinheiro_km = 5.00  # Reais
calculo = km_acima_limite * taxa_dinheiro_km
if (velocidade_carro > 80):
    print(f"Você será multado em R${calculo}.")
    