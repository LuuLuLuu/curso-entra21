"""
4. Escreva uma função chamada "concatenar" que recebe duas strings como parâmetros:
"prefixo" e "sufixo". A função deve retornar a concatenação das duas strings.
"""


def concatenar(str1: str, str2: str) -> str:
    """Esta função pede por dois argumentos, sendo ambos strings, estas strings serão
    concatenadas pelo operador ' + ' e logo em seguida dará o retorno desta operação."""
    return str1 + str2


x = input("Digite uma frase: ")
y = input("Digite outra frase: ")

print(concatenar(x, y))
