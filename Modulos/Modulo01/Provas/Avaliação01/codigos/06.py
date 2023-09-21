x1 = float(input("Me de um número: "))
x2 = float(input("Me de outro número: "))
x3 = float(input("Me de outro número: "))
x4 = float(input("Me de outro número: "))

if x1 < x2 < x3 < x4:
    print(f"{x1:.0f} {x3:.0f} {x2:.0f} {x4:.0f}")
elif x1 < x2 == x3 < x4:
    print(f"{x1:.0f} {x2:.0f} {x3:.0f} {x4:.0f}")
elif x3 == x2+2 and x1 > x4:
    print(f"{x4:.0f} {x1:.0f} {x2:.0f} {x3:.0f}")
elif x1 > x2 and x3 > x4:
    print(f"{x2:.0f} {x1:.0f} {x4:.0f} {x3:.0f}")
