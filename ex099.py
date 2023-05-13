'''99 – Reescreva o código anterior adicionando um mecanismo simples 
de validação que verifica se os dados inseridos pelo usuário são de tipos numéricos, caso não sejam, que o processo seja encerrado.'''

valor_hora = 29.11
hora_extra = 5

try:
    horas = int(input('Digite o número de horas trabalhadas')) * valor_hora
    adicional = float(input('Digite o número de horas extras: ')) * hora_extra

    if horas > 40:
        valor_final = horas + adicional

    else:
        valor_final = horas

except:
    print('Digite apenas números...')
    quit()

print(f'Salário base: R${horas}') 
print(f'Adicional de horas extras: R${adicional}')
print(f'Remuneração Total: R% {valor_final}')