"""
17. Crie um algoritmo que solicite o nome do usuário e informe a quantidade de vogais, 
quantidade de consoantes e o total de caracteres presentes no nome.
"""

nome = input("Digite o seu nome: ").lower()
vogal = 0
consoante = 0

for letra in nome:  # Precisamos iterar pelos caracteres do nome, então use "for letra in nome"
    if letra in "aeiou":  # Verifique se a letra atual está em "aeiou"
        vogal += 1
    else:
        consoante += 1

print(f"O nome {nome.title()} possui {vogal} vogais e {consoante} consoantes.")
