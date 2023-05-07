#78

numero = int(input("Insira um número"))

dicionario = dict()

for i in range(numero+1):
    dicionario[i] = i*i

print(dicionario)