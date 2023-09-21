"""22. Faça um programa que leia o nome de um livro, o tempo médio (em segundos) que o usuário leva para ler
uma página do livro, o tempo de leitura diário (em segundos) e a quantidade de páginas de um livro. Ao final, o
programa deverá mostrar um relatório que mostre:
Quantidade de páginas lidas por dia
Quantidade de horas necessárias para ler o livro
Quantidade de dias necessários para ler o livro
Quantidade de semanas necessárias para ler o livro
"""
# Coleta de dados
livro = input("Digite o título do livro: ")
pg = int(input("Digite a quantidade de páginas do livro: "))
tempo_leitura = float(input("Digite o seu tempo médio de leitura de uma única página(em segundos): "))
tempo_leitura_dia = float(input("Digite o tempo diário de leitura(em segundos): "))

# Cálculo
# Quantidade de tempo
qnt_paginas = tempo_leitura_dia / tempo_leitura
tempo_para_ler = pg * tempo_leitura

qnt_horas = tempo_para_ler / 3600
qnt_dias = tempo_para_ler / 86400
qnt_semanas = tempo_para_ler / 608400

print(f"Tu leu aproximadamente {qnt_paginas} páginas num dia.")
print(f"O livro requer o tempo de leitura de {qnt_horas:.3f} horas.")
print(f"O livro requer o tempo de leitura de {qnt_dias:.3f} dias.")
print(f"O livro requer o tempo de leitura de {qnt_semanas:.3f} semanas.")
