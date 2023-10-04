"""
9. Crie um algoritmo que solicite ao usuário o valor inicial e final de um intervalo de
números e mostre todos os números pares presente nesse intervalo. Caso não haja nenhum
número par o programa deve apresentar a mensagem: “Não há números pares no intervalo”.
"""

inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))
passo = int(input("Digite o passo do intervalo: "))

tem_par = False  # Vai indicar sobre a ideia de ter ou não par

for i in range(inicio, fim + 1, passo):
    if i % 2 == 0:
        print(i, " ")
        tem_par = True

#  Isto só ocorrerá se a linha 16 não for lida.
#  Pois a variável continuará sendo falsa.
if not tem_par:  # O mesmo que: if tem_par == 0
    print("Não há números pares no intervalo.")
