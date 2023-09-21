"""
10. Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este 
número. Isto é, Janeiro se for 1, Fevereiro se 2, e assim por diante.
"""

x = int(input("Digite um número entre 1 e 7: "))

match x:
    case 1:
        print("Janeiro.")
        
    case 2:
        print("Fevereiro.")
        
    case 3:
        print("Terça-feira.")
        
    case 4:
        print("Quarta-feira.")
       
    case 5:
        print("Quinta-feira.")
       
    case 6:
        print("Julho.")
        
    case 7:
        print("Junho.")
        
    case 8:
        print("Agosto.")
        
    case 9:
        print("Setembro.")
        
    case 10:
        print("Outubro.")
        
    case 11:
        print("Novembro.")
        
    case 12:
        print("Dezembro.")
        
