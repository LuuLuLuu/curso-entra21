"""
3. Escreva um programa que peça 5 números inteiros e armazene-os em uma lista. Ao final, 
o programa deve mostrar o menor e o maior número da lista. 
"""

lista = []
for i in range(5):
    x = int(input("Digite um número inteiro: "))
    lista.append(x)

menor = min(lista)
maior = max(lista)

print(f"O menor número na lista é: {menor}")
print(f"O maior número na lista é: {maior}")
