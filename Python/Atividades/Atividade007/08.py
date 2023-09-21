"""
8. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer
correspondentes a duas posições no vetor. Ao final, seu programa deverá escrever a soma dos valores 
encontrados nas respectivas posições X e Y. Se o usuário digitar valores inválidos para X ou Y mostre 
uma mensagem de erro e peça novos valores até que ambos os valores sejam válidos.
"""

vetor = [0] * 8

for i in range(8):
    vetor[i] = int(input(f"Digite o valor para a posição {i}: "))

while True:
    x = int(input("Digite o valor de X (0 a 7): "))
    y = int(input("Digite o valor de Y (0 a 7): "))

    if 0 <= x < 8 and 0 <= y < 8:
        soma = vetor[x] + vetor[y]
        print(f"A soma dos valores nas posições {x} e {y} é {soma}")
        break
    else:
        print("Valores de X e/ou Y são inválidos. Digite novamente.")
