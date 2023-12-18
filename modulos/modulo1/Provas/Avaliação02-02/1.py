"""
1. Escreva uma função chamada compressao_string, que receba uma string como
parâmetro e retorne a versão comprimida da mesma.

Exemplo:
Entrada: “AAABBBCCCCAA”
Saída: “A3B3C4A2”
"""


def compressao_string(s):
    """Utiliza da entrada do usuário para buscar pelo padrão e fazer sua ordenação/compressão."""
    if not s:
        return "Nada foi digitado."

    compresso = ""
    contador = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            contador += 1
        else:
            compresso += s[i - 1] + str(contador)
            contador = 1

    compresso += s[-1] + str(contador)
    return compresso


entrada = input("Digite um texto: ")
saida = compressao_string(entrada).upper()
print(saida)
