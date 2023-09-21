gb = float(input("Digite um valor em GB: "))
mb = gb * 1024
kb = mb * 1024
b = kb * 1024
bit = b * 8

print(f"""
O valor em gigabyte convertido é de:
* {bit}bits
* {b}Bytes
* {kb}KB
* {mb}MB
""")
