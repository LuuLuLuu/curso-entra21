"""
5. Escreva uma função chamada “repetir” que recebe dois parâmetros. O primeiro é o
elemento que repetirá, enquanto o segundo é o número de vezes que haverá a repetição.
Uma lista deve ser retornada.
"""


def repetir(x: int, y: int) -> list[str]:
    """Esta função criará uma lista, a qual recebe um argumento x que será armazenado
    seguido de um contador de em qual iteração ela foi inserida na lista. A função
    retornará a lista."""
    lista = []

    for i in range(y):
        lista.append(f"{x} - {i+1}")

    return lista


print(repetir(1, 9))
