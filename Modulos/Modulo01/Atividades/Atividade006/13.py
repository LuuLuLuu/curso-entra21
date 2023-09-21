"""
13. Escreva um programa que calcule o quociente da divisão de dois números. O programa deve receber
o dividendo e o divisor e realizar operações de subtração com laços de repetição para chegar ao 
valor esperado.
"""
x1 = int(input("Digite o dividendo: "))
x2 = int(input("Digite o divisor: "))

if x2 != 0:
    quociente = 0
    while x1 >= x2:
        x1 -= x2
        quociente += 1
    print(f"O quociente da divisão é: {quociente}")
