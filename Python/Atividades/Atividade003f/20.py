horas = float(input("Digite uma quantidade de tempo em horas: "))
minutos = float(input("Digite uma quantidade de tempo em minutos: "))
segundos = float(input("Digite uma quantidade de tempo em segundos: ")) + minutos * 60 + horas * 60**2

print(f"O tempo dado, convertido para segundos é de {segundos} segundos.")
