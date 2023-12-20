# 3. Escreva uma função que receba uma lista de números e retorne o maior valor 
# da lista. Em seguida, escreva um teste usando pytest para verificar se a 
# função está retornando corretamente o maior valor.

x = {2,5,6,7,1,2,9,10,9999999}


def max_number(a:list) -> int:
    return max(a);

print(max_number(x))