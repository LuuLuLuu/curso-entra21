"""
16. Utilizando os conceitos de matrizes e laços de repetição faça um jogo da velha onde a cada rodada 
será pedido a posição onde o jogador X quer jogar e onde o jogador O quer jogar. Caso seja informado 
uma posição já ocupada, informe que a "posição já está ocupada" e peça por outra jogada. Quando o jogo 
acabar mostrar quem ganhou o jogo, ou em caso de empate, a mensagem: "O jogo empatou".
"""

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

jogador_atual = "X"

for rodada in range(9):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

    print(f"É a vez do jogador {jogador_atual}.")

    linha = int(input("Informe a linha (0, 1 ou 2): "))
    coluna = int(input("Informe a coluna (0, 1 ou 2): "))

    if tabuleiro[linha][coluna] != " ":
        print("Posição já está ocupada. Tente novamente.")
        continue

    tabuleiro[linha][coluna] = jogador_atual

    for linha in tabuleiro:
        if all(simbolo == jogador_atual for simbolo in linha):
            print(f"O jogador {jogador_atual} ganhou o jogo!")
            exit()

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador_atual for linha in range(3)):
            print(f"O jogador {jogador_atual} ganhou o jogo!")
            exit()

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador_atual:
        print(f"O jogador {jogador_atual} ganhou o jogo!")
        exit()
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador_atual:
        print(f"O jogador {jogador_atual} ganhou o jogo!")
        exit()

    jogador_atual = "O" if jogador_atual == "X" else "X"

for linha in tabuleiro:
    print(" | ".join(linha))
    print("-" * 9)
print("O jogo empatou.")
