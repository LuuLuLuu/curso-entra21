"""
9. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene 
os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use 
um vetor de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.
"""

import random

contadores = [0] * 6

for _ in range(100):
    resultado = random.randint(1, 6)
    
    contadores[resultado - 1] += 1

for valor, contador in enumerate(contadores, start=1):
    print(f"Valor {valor}: {contador} vezes")
