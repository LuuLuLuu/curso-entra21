"""
2. Crie uma função chamada "dobro" que recebe um número como parâmetro e retorna
o dobro desse número. Inclua uma docstring que explique o propósito da função.
"""


def dobro(x: int):
    """Realiza o print() do dobro de um número dado pelo usuário.
    O input tem de pedir por um número inteiro."""
    print(f"O dobre de {x} é {x * 2}.")


num = int(input("Digite um número inteiro: "))
dobro(num)
