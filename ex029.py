'''29 - Crie um programa que lê um valor de início e um valor de fim exibindo em tela a contagem dos números dentro desse intervalo'''

valor_inicio = int(input('Insira um valor inicial: '))
valor_final = int(input('Insira um valor final: '))

'''while valor_inicio != valor_final:
    print(valor_inicio + 1)
    valor_inicio += 1'''
    
for i in range(valor_inicio, valor_final):
    print(valor_inicio + 1)
    valor_inicio += 1