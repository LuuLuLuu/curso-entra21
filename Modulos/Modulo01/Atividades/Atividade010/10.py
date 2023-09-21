"""
10. Escreva uma função “formata_cpf” que recebe um número inteiro e converta ele para uma string no 
formato do cpf “000.000.000-00”. Caso o número fornecido não seja válido a função deve retornar o 
próprio número em formato de string.
"""
import regex as re


def formata_cpf(numero):
    """
    Pede pelo CPF como parâmetro e o transforma para string utilizando de regex. Ve se o número é válido
    pelo tamanho do número do CPF dado.
    """
    cpf = re.sub(r'\D', '', str(numero))

    if len(cpf) == 11:
        cpf_formatado = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
        return cpf_formatado
    else:
        return str(numero)


print(formata_cpf(12345678900))  # Saída: "123.456.789-00"
print(formata_cpf(12345))  # Saída: "12345" (não é um CPF válido)
