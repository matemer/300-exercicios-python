'''34 - Crie um programa que realiza a contagem de 1 até 100, usando apenas de
 números ímpares, ao final do processo exiba em tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos'''
 
contagem = 0
soma = 0

for i in range(1,101):
     if i % 2 != 0:
         contagem += 1
         print(i)
         soma += i
         
print(f'A quantidade de números ímpares encontrados foram {contagem}')
print(f'A soma destes números foram {soma}')
     