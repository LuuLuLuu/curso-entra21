salario_anual = float(input("Digite seu salário anual: "))
meta = (float(input("Digite a meta recebida: ")))
meta_atigindia = float(input("Digite o quanto da meta tu atingiu: "))

if meta_atigindia >= meta:
    bonus = 20
    calculo = bonus / 100 * salario_anual
    print(f"O valor do bônus a receber é de {calculo}.")
elif meta_atigindia >= meta/2:
    bonus = 10
    calculo = bonus / 100 * salario_anual
    print(f"O valor do bônus a receber é de {calculo}.")
else:
    print("Este funcionário não receberá bônus algum.")
