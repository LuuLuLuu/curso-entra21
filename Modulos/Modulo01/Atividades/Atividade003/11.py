num = float(input("Digite um número: "))

if num < 0:
    print(f"""
    O antecessor do número {num:.0f} é {num+1:.0f}.
    O sucessor do número {num:.0f} é {num-1:.0f}.
    """)
elif num >= 0:
    print(f"""
    O antecessor do número {num:.0f} é {num-1:.0f}.
    O sucessor do número {num:.0f} é {num+1:.0f}.
    """)
