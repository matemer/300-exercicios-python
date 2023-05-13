'''97 – Escreva de forma reduzida um programa que recebe do usuário um nome e duas notas, salvando tais dados como um elemento de uma lista. Exiba em tela o conteúdo dessa lista.'''

from operator import itemgetter

nomes = []

while True:
    dados = input('Digite seu nome, seguido de duas notas de 0 a 10: ')
    if not dados:
        break
    nomes.append(tuple(dados.split(',')))

print(sorted(nomes,key = itemgetter(0,1,2)))