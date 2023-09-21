"""
12. Dada uma lista de números inteiros, escreva um programa que encontre a soma dos números 
consecutivos maiores do que zero. Por exemplo, para a lista [ -2, 3, 4, 0, 7, -1], o programa deve 
retornar a soma 7 (3 + 4)
"""
numeros = [-2, 3, 4, 0, 7, -1]
soma = 0
numero_anterior = 0

for numero in numeros:
    if numero > 0 and numero_anterior > 0:
        soma += numero
    
    numero_anterior = numero

print("A soma dos números consecutivos maiores do que zero é:", soma)
