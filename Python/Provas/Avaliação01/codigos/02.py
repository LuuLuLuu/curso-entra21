import math

print("Escolha sua operação:")
print("(+) para adição;")
print("(-) para subtração;")
print("(x) para multiplicação;")
print("(/) para divisão;")
print("(%) para porcentagem;")
print("(Log) para logaritmo.")
operacao = input("Digite a operação escolhida: ")

num1 = ""
num2 = ""

if operacao == "Log":
    num1 = float(input("Digite um número: "))
    base = float(input("Digite a base do logaritmo: "))

    print(math.log(num1, base))

    exit()

if operacao == "%":
    num1 = float(input("Digite um número: "))
    porcentagem = float(input("Digite a porcentagem: "))

    print(num1 * porcentagem/100)

if operacao != "Log":
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um segundo número: "))

match operacao:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2:.2f}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2:.2f}")
    case "x":
        print(f"{num1} * {num2} = {num1 * num2:.2f}")
    case "/":
        print(f"{num1} / {num2} = {num1 / num2:.2f}")
