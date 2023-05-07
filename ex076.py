#076

valor1 = int(input('Qual o primeiro número'))
valor2 = int(input('Qual o segundo número'))

sinal = str(input("Qual o sinal: [+,-,*,/]"))

if sinal == '+':
    print(valor1+valor2)

elif sinal == '-':
    print(valor1 - valor2)

elif sinal == '*':
    print(valor1 * valor2)

elif sinal == '/':
    print(valor1 / valor2)