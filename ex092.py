'''92 – Crie um programa que recebe do usuário uma sequência de números aleatórios separados por vírgula, armazene os números um a um, em formato de texto, como elementos ordenados de uma lista. Mostre em 
tela a lista com seus respectivos elementos após ordenados.'''

numeros = input("Insira os valores dos numeros: ")

lista = numeros.split(",")

lista.sort()

print(lista)