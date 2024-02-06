"""
4. Escreva um programa que pergunte a distância que um passageiro 
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 
por km para viagens de até de 200km, e R$ 0,45 para viagens mais longas.
"""

distancia_km = int(input("Qual a distância e Km que tu deseja percorrer: "))
if (distancia_km <= 200):
    preco_passagem = distancia_km * 0.50
else:
    preco_passagem = distancia_km * 0.45

print(f"O preço da passagem será: R${preco_passagem}.")
