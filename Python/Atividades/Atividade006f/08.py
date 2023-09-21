"""
8. Um restaurante de fast-food oferece um menu com 4 opções de hambúrgueres: X-Burger, X-Salada, X-Bacon e X-Tudo.
Cada hambúrguer tem um preço diferente: R$10, R$12, R$15 e R$18, respectivamente. Escreva um programa que solicite
ao usuário a quantidade desejada de cada hambúrguer e exiba o valor total do pedido.
"""

x_burguer = 10
x_salada = 12
x_bacon = 15
x_tudo = 18

soma = 0

while True:
    comanda = input(""""
    Digite o hamburger desejado: 
    x-burguer - R$10,00
    x-salada - R$12,00
    x-bacon - R$15,00
    x-tudo - R$18,00
    """)
    quantidade = int(input("Digite a quantidade do hamburger desejado: "))
    match comanda:
        case "x-burguer":
            soma += x_burguer * quantidade
        case "x-salada":
            soma += x_salada * quantidade
        case "x-bacon":
            soma += x_bacon * quantidade
        case "x-tudo":
            soma += x_tudo * quantidade
    continuar = input(""""
    Deseja anotar outro pedido? 
    Sim(S) ou não(N)?
    """)
    if continuar == "S":
        continue
    else:
        break

print(f"A soma total dos pedidos é de: {soma}.")
