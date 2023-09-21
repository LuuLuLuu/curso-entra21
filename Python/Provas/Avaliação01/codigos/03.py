ano = int(input("Digite um ano: "))

if ano % 4 == 0:  # 1 para 2
    if ano % 100 == 0:  # 2 para 3
        if ano % 400 == 0:  # 3 para 4
            print("O ano é bissexto.")
        else:  # 3 para 5
            print("O ano não é um ano bissexto.")
    else:  # 2 para 4
        print("O ano é bissexto.")
else:  # 1 para 5
    print("O ano não é um ano bissexto.")
