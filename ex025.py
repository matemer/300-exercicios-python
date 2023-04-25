'''25 - Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem dizendo se tal número é PAR ou ÍMPAR'''

numero = int(input('Insira um número: '))

if numero%2 == 0:
    print('O número é PAR')
else:
    print('O número é ÍMPAR')