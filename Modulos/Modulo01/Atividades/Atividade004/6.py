"""
6. Escreva um programa que receba um número, se esse número estiver entre 20 e 90 mostre na 
tela a mensagem “O número está na faixa entre 20 e 90”, se não, mostre “O número está fora da faixa”.
"""

x = float(input("Digite um número: "))

if 20 <= x <= 90:
    print("O número está na faixa entre 20 e 90.")
else:
    print("O número está fora da faixa.")
