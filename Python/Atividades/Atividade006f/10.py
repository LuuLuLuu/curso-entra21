"""
10. Crie um algoritmo que realize a leitura de 5 números inteiros e ao final mostre qual
é o maior e o menor número lido. Suponha que nem todos os números serão positivos.
"""

x = []
for _ in range(5):
    x.append(int(input("Digite um número inteiro: ")))

print(f"O menor número dado é {min(x)} e o maior é {max(x)}")
