peso = float(input("Digite o quanto você pesa, em kg: "))
altura = float(input("Digite a sua altura, em metros: "))

imc = peso / altura**2
# print(imc) --> utilizei para teste
print(f"Teu imc é de {imc:.2f}kg/m²...")

if imc < 18.5: # imc < 18.5
    print("... com este IMC tu está abaixo do peso.")
elif imc <= 24.9: # imc entre 18.5 e 24.9
    print("... com este IMC tu está com o peso normal.")
elif imc <= 29.9: # imc entre 25 e 29.9
    print("... com este IMC tu está com sobrepeso.")
elif imc <= 34.9: # imc entre 30 e 34.9
    print("... com este IMC tu está com obesidade de grau 1.")
elif imc <= 39.9: # imc entre 35 e 29.9
    print("... com este IMC tu está com obesidade de grau 2.")
else: # É considerado que seja maior ou igual que 40
    print("... com este IMC tu está com obesidade de grau3.")

"""
Imagino que a formatação do IMC para possuir apenas duas casas decimais seja referente 
apenas no texto, pois em comparação é irrelevante, pois idependente das casas decimais a
comparação será certeira, a não ser de por algum acaso de um IMC de dizima periódica 
de 9(0,999...) o que todo mundo sabe que é um, ou seja, viria a arredondar para cima, 
mas isso eu não sei resolver. Isso se o python arredondar.
"""
