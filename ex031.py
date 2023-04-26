'''31 - Crie um programa que realiza a progressão aritmética de 20 elementos
, com primeiro termo e razão definidos pelo usuário'''

primeiro_termo = int(input('insira o primeiro termo: '))
razao = int(input('insira a razão: '))

enesimo_termo = primeiro_termo + (20 - 1) * razao

for i in range(primeiro_termo, enesimo_termo + razao, razao):
    print(i)