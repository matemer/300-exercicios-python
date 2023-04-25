'''24 - Crie duas variáveis com dois valores numéricos inteiros digitados pelo usuário, caso o valor do primeiro número for maior que o do segundo, exiba em tela uma
mensagem de acordo, caso contrário, exiba em tela uma mensagem dizendo que o primeiro valor digitado é menos que o segundo'''

variavel1 = int(input('Insira o primeiro valor: '))
variavel2 = int(input('Insira o segundo valor: '))

if variavel1 > variavel2:
    print('a variavel 1 é maior que a variavel 2')
    
else:
    print('o primeiro número digitado não é o maior')