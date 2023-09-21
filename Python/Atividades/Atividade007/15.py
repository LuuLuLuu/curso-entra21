"""
15. Escreva um programa que receba uma lista como entrada e retorne uma nova lista comprimida, onde
elementos repetidos sejam substituídos por uma tupla contendo o elemento e a quantidade de vezes que
ele se repete. Por exemplo, para a lista [1, 1, 1, 2, 3, 3, 4, 4, 4, 4], o programa deve retornar 
[(1, 3), 2, (3, 2), (4, 4)].
"""

entrada = input("Digite uma lista de elementos separados por espaços: ")
elementos = entrada.split()
resultado_comprimido = []
elemento_atual = None
contagem = 0

for elemento in elementos:
    if elemento != elemento_atual:
        if elemento_atual is not None:
            resultado_comprimido.append((elemento_atual, contagem))
        elemento_atual = elemento
        contagem = 1
    else:
        contagem += 1

if elemento_atual is not None:
    resultado_comprimido.append((elemento_atual, contagem))

print(resultado_comprimido)
