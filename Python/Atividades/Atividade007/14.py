"""
14. Crie um algoritmo que receba duas listas como parâmetros e retorne uma nova lista contendo os elementos
intercalados das duas listas. Por exemplo, se as listas forem `[1, 2, 3]` e `[4, 5, 6]`, o algoritmo deve 
retornar `[1, 2, 3, 4, 5, 6]`.
"""

# Defina duas listas de exemplo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Inicialize uma lista vazia para armazenar o resultado intercalado
resultado = []

# Determine o tamanho mínimo entre as duas listas
tamanho_minimo = min(len(lista1), len(lista2))

# Intercale os elementos das duas listas até o tamanho mínimo
for i in range(tamanho_minimo):
    resultado.append(lista1[i])
    resultado.append(lista2[i])

# Adicione os elementos restantes da lista mais longa (se houver)
if len(lista1) > len(lista2):
    resultado.extend(lista1[tamanho_minimo:])
elif len(lista2) > len(lista1):
    resultado.extend(lista2[tamanho_minimo:])

# Exiba o resultado intercalado
print(resultado)
