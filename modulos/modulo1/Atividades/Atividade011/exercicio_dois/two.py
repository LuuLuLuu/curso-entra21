# 2. Escreva uma função que verifique se um número é par. 
# Em seguida, escreva um teste usando pytest para verificar se a 
# função está retornando corretamente True para números pares e 
# False para números ímpares.


def pair(a:int) -> bool:
    if a % 2 == 0:
        return True;
    else:
        return False;

