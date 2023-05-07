#82
def inverte_nome(n):
    nome,sobrenome = n.split()
    return ' '.join([sobrenome,nome])

nome = input('insira seu nome e sobrenome')

pessoa = inverte_nome(nome)

print(pessoa)