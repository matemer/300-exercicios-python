'''36 - Crie um programa que pede que o usuário digite um npme ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo na tela esse resultado'''

frase = str(input('Insira um texto: ')).strip().upper()
palavras = frase.split()
caracteres = ''.join(palavras)
fraseinvertida = ''

for i in range(len(caracteres) - 1, -1, -1):
    fraseinvertida += caracteres[i]
    
print(caracteres, fraseinvertida)

if fraseinvertida == caracteres:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')