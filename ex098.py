'''98 – Crie um programa que gera o valor de salário de funcionários considerando apenas horas trabalhadas e horas extras, sendo o valor fixo
 da hora trabalhada R$29,11 e da hora extra R$5,00. Crie uma regra onde o funcionário só tem direito a receber 
horas extras a partir de 40 horas trabalhadas da forma convencional.'''

valor_hora = 29.11
hora_extra = 5

horas = int(input("Quantas horas foram trabalhadas: ")) * valor_hora
adicional = int(input("Quantas horas adicionais: ")) * hora_extra

if horas > 40:
    valor_final = horas + adicional

else:
    valor_final = horas

print(f'Salário base: {horas}')
print(f'Salário adicional: {adicional}')