"""
18. Faça um algoritmo que simule uma calculadora. Para isso, o algoritmo deverá solicitar dois 
números e a operação matemática que deve ser executada. O algoritmo deve permitir as operações
de adição, subtração, multiplicação e divisão.
"""

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operacao = input("Digite o operador (+, -, /, *): ")

match operacao:
    case "+":
        print(f"A soma (+) entre {n1} e {n2} é igual a {n1+n2}")
    case "-":
        print(f"A subtração (-) entre {n1} e {n2} é igual a {n1-n2}")
    case "*":
        print(f"A multiplicação (*) entre {n1} e {n2} é igual a {n1*n2}")
    case "/":
        print(f"A divisão (*) entre {n1} e {n2} é igual a {n1/n2}")
