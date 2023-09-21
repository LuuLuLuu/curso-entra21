"""
16. Escreva um algoritmo que peça o salário bruto de uma pessoa e imprima o salário líquido, segunda a tabela a seguir:

Salário bruto menor ou igual a R$ 600.00
Isento

Salário bruto maior que R$ 600.00 e menor ou igual a R$ 1200.00
20%

Salário bruto maior que R$ 1200.00 e menor ou igual a R$ 2000.00
25%

Salário bruto maior que R$ 2000.00
30%
"""

salario_bruto = float(input("Informe o salário bruto: "))

if salario_bruto <= 600:
    print("Tu esta isento de qualquer desconto de seu salário liquído.")
elif salario_bruto <= 1200:
    salario_liquido_20 = salario_bruto - salario_bruto * 0.20
    print(f"Tu esta sujeito a um desconto de 20% de seu salário liquído, passando a receber {salario_liquido_20}")
elif salario_bruto <= 2000:
    salario_liquido_25 = salario_bruto - salario_bruto * 0.25
    print(f"Tu esta sujeito a um desconto de 25% de seu salário liquído, passando a receber {salario_liquido_25}")
else:
    salario_liquido_30 = salario_bruto - salario_bruto * 0.30
    print(f"Tu esta sujeito a um desconto de 30% de seu salário liquído, passando a receber {salario_liquido_30}")
