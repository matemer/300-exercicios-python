'''91 – Escreva um programa que recebe uma frase qualquer, mapeando a mesma e retornando ao usuário cada palavra com a frequência com que a mesma aparece na frase em questão.
Feltrin, Fernando. 300 Exercícios Resolvidos e Comentados em Python (p. 149). Edição do Kindle. '''

frequencia = {}

texto = 'Estou tentando entender como usar o get, usando palavras aleatórias agora'

for palavra in texto.split():
    frequencia[palavra] = frequencia.get(palavra,0) + 1

palavras = frequencia.keys()

for i in palavras:
    print(f'{i} = {frequencia[i]}')