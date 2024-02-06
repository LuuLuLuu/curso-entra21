"""
5. Escreva um programa para aprovar o empréstimo bancário para compra 
de uma casa. O programa deve perguntar o valor da casa a comprar, 
o salário e a quantidade de anos a pagar. O valor da prestação mensal
não pode ser superior a 30% do salário. Calcule o valor da prestação 
como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""

valor_casa = int(input("Informe o valor da casa: "))
salario = int(input("Informe seu salário: "))
anos = int(input("Informe a quantidade de anos para pagar a casa: "))

meses = anos * 12
prestacao = valor_casa / meses
limite_prestacao = 0.3 * salario

print(f"30% do seu salário é R${limite_prestacao:.2f}.")

if prestacao > limite_prestacao:
    print("Empréstimo não aprovado. A prestação excede 30% do salário.")
else:
    print(f"A prestação mensal fica em R${prestacao:.2f}. Empréstimo aprovado!")