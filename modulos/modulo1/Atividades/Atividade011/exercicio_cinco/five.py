# 5. Escreva uma função que receba uma lista de strings e retorne uma lista contendo 
# o tamanho de cada string. Em seguida, escreva um teste usando pytest para verificar
# se a função está retornando corretamente a lista de tamanhos.


list = ['Hellow World!', 'Ozymandias', 'E=mc2']


def list_len(a) -> list:
    return [len(a[0]), len(a[1]), len(a[2])];


print(list_len(list));