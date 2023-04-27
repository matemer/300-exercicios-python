#59

def pessoa(nome, idade = 18, nacionalidade = 'Brasileiro'):
    print(f'Bem vindo, {nome}! Você tem {idade} e é {nacionalidade}.')
    
nome = input("Qual o seu nome: ")
pessoa(nome, nacionalidade = 'Português')
    