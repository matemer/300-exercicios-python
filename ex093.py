'''93 – Escreva um programa, da forma mais reduzida o possível, que recebe do usuário uma série de nomes, separando os mesmos e os organizando em ordem alfabética. Em seguida, exiba em tela os nomes já ordenados.'''

nomes = input('Insira alguns nomes separando por ,: ').split(',')

nomes.sort()

print(nomes)