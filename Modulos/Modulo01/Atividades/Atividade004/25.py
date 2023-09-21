""""
25. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. O programa
deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
- Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informa ao usuário;
- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
a = float(input("Digite um valor para A: "))

if a == 0:
    exit()
elif a != 0:
    b = float(input("Digite um valor para B: "))
    c = float(input("Digite um valor para C: "))
    delta = b**2 -4 * a * c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        print("A equação possui apenas uma raíz real")
    elif delta > 0:
        print("A equação possui duas raíz reais")
