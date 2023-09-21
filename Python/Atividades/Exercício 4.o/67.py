a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

r1 = "1"

if a == 0:
    print("A equação não é do segundo grau.")
else:
    d = b**2 - 4 * a * c
    if d < 0:
        print("A equação não possui raízes reais.")
    elif d == 0:
        r0 = -b/(2*a)
    print("Raíz:", r0)
    else:
        r1 = (-b+d)/(2*a)
        r2 = (-b-d)/(2*a)
        print("Raíz 1:", r1)
        print("Raíz 2:", r2)
