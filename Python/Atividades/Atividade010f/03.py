"""
3. Crie uma função chamada "apresentacao" que recebe o nome de uma pessoa como parâmetro e
imprime uma saudação personalizada. Se nenhum nome for fornecido, a saudação deve ser
genérica como "Olá, amigo!".
"""


def apresentacao(nome="amigo"):
    """Realizará o print() junto do argumento entregue, caso não seja dado argumento algum,
    será utilizado do parâmetro padrão para completar o print()."""

    print(f"Olá, {nome}!")


apresentacao("Luis")  # Se nenhum argumento for entregue, a saída será "amigo".
