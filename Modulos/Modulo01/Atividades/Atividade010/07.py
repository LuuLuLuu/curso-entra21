"""
7. Defina uma função chamada "calcular_area" que recebe dois parâmetros: "base" e "altura". Adicione 
anotações de função para indicar que os parâmetros são números e que a função retorna um número.
"""


def calcular_area(base: float, altura: float) -> float:
    """
    Calcula a área de um retângulo.

    :param base: A base do retângulo (um número)
    :param altura: A altura do retângulo (um número)
    :return: A área do retângulo (um número)
    """
    area = base * altura
    return area


print(calcular_area(4, 7))
