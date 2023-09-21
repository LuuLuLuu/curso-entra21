"""
4. Crie um programa que receba o nome, idade, peso, altura e telefone do usuário e mostre na tela 
as informações no seguinte formato:
Nome: <nome:
Idade: <idade>
Peso: <peso>
Altura: <altura>
Telefone: <telefone>

"""

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
peso = int(input("Digite o peso: "))
altura = int(input("Digite a altura em centimetros: "))
telefone = input("Digite o telefone: ")

print(f"""
Nome: {nome}
Idade: {idade}
Peso: {peso}
Altura: {altura}
Telefone: {telefone}
""")
