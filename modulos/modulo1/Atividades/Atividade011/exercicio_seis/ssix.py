# 6. Escreva uma função que receba uma lista de números e retorne a soma de todos os 
# números pares da lista. Em seguida, escreva um teste usando pytest para verificar 
# se a função está retornando corretamente a soma dos números pares.

def sum_pair(a:list) -> int:
    x = 0;

    for i in range(len(a)):
        if a[i] % 2 == 0:
            x += a[i];
        else: 
            pass;
    
    return x;