'''35 - Crie um programa que pede ao usuário que o mesmo digite um número qualquer,
em seguida retorne se esse número é primo ou não, caso não retorne também quantas vezes esse número é divisivel'''

num = int(input('Insira um número: '))
divisoes = 0

for i in range(1, num + 1):
    if num % i == 0:
        divisoes += 1
        
if divisoes == 2:
    print('É um número primo')
    print(f'É divisivel {divisoes} vezes')
    
else:
    print('Não é um número primo')
    print(f'É divisivel {divisoes} vezes')