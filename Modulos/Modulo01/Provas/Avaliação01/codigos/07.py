dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

if dia < 0 or mes < 0 or ano < 0:
    print("A data informa está incorreta.")
    exit()

if mes < 13:
    if ano % 4 == 0 or ano % 100 == 0 or ano % 400 == 0:  # Verificando se é bissexto.
        if dia == 29:
            print(f"É um ano bissexto.")
            print(f"A data informada {dia}/{mes}/{ano} é valida.")
            exit()
        elif dia <= 28:
            print(f"É um ano bissexto.")
            print(f"A data informada {dia}/{mes}/{ano} é valida.")
            exit()
        elif dia > 29:
            print("A data informa está incorreta.")
            exit()

    elif dia > 29:
        print("A data informa está incorreta. a")
        exit()
    print(f"A data informada {dia}/{mes}/{ano} é valida.")
else:
    print("A data informa está incorreta.")
