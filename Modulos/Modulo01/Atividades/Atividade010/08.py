"""
8. Crie uma função chamada "somar" que recebe uma quantidade variável de números como 
argumentos e retorna a soma deles.
"""

def somar() -> float:
    """
    Um laço infinito para verificar se o usu;ario quer continuar fazendo alguma operação, 
    senão uma variável vai se incrementar com o número digitado para se ter o retorno da soma.
    """
    y = 0 
    while True:
        x = input("Digite um número (ou 'X' para sair): ")
        if x.upper() == 'X': 
            break
        y += float(x)

    return y


print(somar())
