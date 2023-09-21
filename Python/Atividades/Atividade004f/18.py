"""
19. Faça um algoritmo que calcule o peso de uma pessoa em outros planetas. Para isso o programa 
deve solicitar o peso da pessoa, em qual planeta ela deseja saber o seu peso e utilizar a seguinte 
escala de gravidade dos planetas em relação a terra:
Mercúrio: 0.38
Vênus: 0.91
Marte: 0.38
Júpiter: 2.34
Saturno: 0.93
Urano: 0.92
Netuno: 1.12
Plutão: 0.06
"""

peso = float(input("Informe seu peso: "))
planeta = input("Em qual palneta você deseja saber o seu peso?: ").upper()

match planeta:
    case "MERCÚRIO":
        print(f"Seu peso em Mercúrio é igual a {peso*0.38}")
    case "VÊNUS":
        print(f"Seu peso em Vênus é igual a {peso*0.91}")
    case "MARTE":
        print(f"Seu peso em Marte é igual a {peso * 0.38}")
    case "JÚPITER":
        print(f"Seu peso em Júpiter é igual a {peso * 2.34}")
    case "SATURNO":
        print(f"Seu peso em Saturno é igual a {peso * 0.93}")
    case "URANO":
        print(f"Seu peso em Urano é igual a {peso * 0.92}")
    case "NETUNO":
        print(f"Seu peso em Netuno é igual a {peso * 1.12}")
    case "PLATÃO":
        print(f"Seu peso em Platão é igual a {peso * 1.06}")
