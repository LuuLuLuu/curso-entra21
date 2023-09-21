"""
2. Escreva um programa que peça as três notas de um aluno armazenando-as em uma lista e retorne
a média das notas.
"""

notas = []

notas.append(float(input("Digite a primeira nota: ")))
notas.append(float(input("Digite a segunda nota: ")))
notas.append(float(input("Digite a terceira nota: ")))

soma_notas = sum(notas)
media = soma_notas / len(notas)

print(f"A média do aluno é {media:.2f}")
