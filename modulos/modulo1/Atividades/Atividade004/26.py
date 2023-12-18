"""
26. Crie um programa que auxilie no controle de gastos pessoais. Peça ao usuário para inserir suas despesas mensais nas seguintes categorias:
Alimentação
Moradia
Transporte
Lazer
Saúde
TV / Internet / Telefone
Também peça ao usuário o seu salário mensal. O programa deve calcular o total de despesas, mostrar o percentual de cada categoria em relação ao total e informar se as suas despesas excedem o salário.
"""

gastos = {
    "salario": int(input("Informe o seu salário: ")),
    "alimentacao": int(input("Informe o seu gasto com alimentação: ")),
    "moradia": int(input("Informe o seu gasto com as despesas de sua casa: ")),
    "transporte": int(input("informe o seu gasto com transporte: ")),
    "lazer": int(input("Informe o seu gasto com lazer: ")),
    "saude": int(input("Informe o seu gasto com saúde: ")),
    "telefone": int(input("Informe o seu gasto com a conta de telefone: "))
}

print(gastos)

despesa_total = gastos["alimentacao"] + gastos["moradia"] + gastos["transporte"] + gastos["lazer"] + gastos["saude"] + gastos["telefone"]
print(despesa_total)

porcentagem_alimentacao =  gastos["alimentacao"] / despesa_total * 100
print(f"Alimentacao -> {porcentagem_alimentacao:.2f}%")
porcentagem_moradia =  gastos["moradia"] / despesa_total * 100
print(f"Moradia -> {porcentagem_moradia:.2f}%")
porcentagem_transporte =  gastos["transporte"] / despesa_total * 100
print(f"Transporte -> {porcentagem_transporte:.2f}%")
porcentagem_lazer =  gastos["lazer"] / despesa_total * 100
print(f"Lazer -> {porcentagem_lazer:.2f}%")
porcentagem_saude =  gastos["saude"] / despesa_total * 100
print(f"Saude -> {porcentagem_saude:.2f}%")
porcentagem_telefone =  gastos["telefone"] / despesa_total * 100
print(f"Telefone -> {porcentagem_telefone:.2f}%")


if despesa_total > gastos["salario"]:
    print("Você gasta mais doque recebe!")
else:
    print("Tu está com o gasto controlado.")
