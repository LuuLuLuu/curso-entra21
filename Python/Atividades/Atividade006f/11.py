"""
11. Vamos criar um jogo de adivinhação de números! O programa irá gerar um número aleatório
 entre 1 e 100, e o jogador terá que adivinhar qual é esse número. O programa deve fornecer
  dicas ao jogador, informando se o número a ser adivinhado é maior ou menor do que o número
   fornecido pelo jogador. O jogo deve continuar até o jogador adivinhar corretamente o número.
"""

import random

num = random.randrange(1, 100)

while True:
    adivinha = int(input("Adivinhe um número de 1 a 100: "))

    if adivinha <= 0:
        print("O número gerado é maior que zero.")
        continue
    elif adivinha > 100:
        print("O número gerado é menor que cento e um.")
        continue
    elif adivinha < num:
        print("O número digitado é menor que o número gerado.")
        continue
    elif adivinha > num:
        print("O número digitado é maior que o número gerado.")
        continue
    else:
        exit()
