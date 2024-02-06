"""
2. Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 11 minutos de vida a cada cigarro, calcule 
quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

qnt_cigarros_dia = int(input("Digite quantos cigarros são fumados por dia: "))
qnt_anos_sendo_fumante = int(input("Digite a quantos anos a pessoa é fumante: "))
perda_vida_minutos_cigarro = 11
calculo = qnt_cigarros_dia * perda_vida_minutos_cigarro / 1440 * qnt_anos_sendo_fumante
print(f"O fumante que fuma {qnt_cigarros_dia} cigarros por dia a {qnt_anos_sendo_fumante} anos ao todo perdeu por volta de {calculo * 100:.2f} dias de vida.")
