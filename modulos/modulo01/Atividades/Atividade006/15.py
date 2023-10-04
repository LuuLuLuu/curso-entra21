"""
15. Crie um algoritmo que leia o nome e as três notas de 5 alunos e mostre a média de cada um deles. 
Ao final mostre a média da turma.
"""

media_turma = 0

for i in range(5):
    aluno = input("Digite o nome do aluno: ")
    for i in range(1):
        nota1 = int(input("Digite a primeira nota: "))
        nota2 = int(input("Digite a segunda nota: "))
        nota3 = int(input("Digite a terceira nota: "))
        media = (nota1 + nota2 + nota3) / 3
        media_turma += media
        print(f"A média das notas do aluno(a) {aluno} é {media:.2f}.")
        break
 
print(f"A média da turma é de {media_turma / 5:.2f}.")
