"""
11. Faça um programa que pergunte em que turno você estuda. Peça para digitar M - Matutino, 
V - Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!" ou 
"Valor Inválido!" de acordo com o turno escolhido
"""

turno = input("""
              Digite o seu turno:
              M - Matutino
              V - Vespertino
              N - Noturno
              """)

match turno:
    case "M":
        print("Bom Dia!")

    case "V":
        print("Boa Tarde!")

    case "N":
        print("Boa Noite!")

    case _:
        print("Valor inválido")