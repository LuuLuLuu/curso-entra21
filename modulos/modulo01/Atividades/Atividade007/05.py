"""
5. Dada uma lista de nomes, crie uma nova lista que contenha apenas os nomes que começam com a letra “A”.
"""

nomes = ["Luis", "Ana", "Maria", "William", "Pedro", "Alice", "Alberto", "Paula"]

nomes_com_a = [nome for nome in nomes if nome.startswith("A")]

print(nomes_com_a)
