'''100 – Crie um programa que recebe uma nota entre 0 e 1.0, 
classificando de acordo com a nota se um aluno fictício está aprovado ou em recuperação de acordo com sua 
nota. A média para aprovação deve ser 0.6 ou mais, e o programa deve 
realizar as devidas validações para caso o usuário digite a nota em um formato inválido.'''

def calcula_nota(nota):
    if nota < 0 or nota > 1.0:
        print('Pontuação inválida!')
        print('A nota deve ser um valor entre 0 e 1')
    elif nota == 1.0:
        print('Parabéns, você gabaritou a prova!')
    elif nota >= 0.6:
        print('parabéns, você foi aprovado(a)!')
    elif nota<0.6:
        print('Nota abaixo da média, você esta em recuperação!')
    else:
        print('Não foi possível computar sua nota')

try:
    nota = float(input("Digite uma nota: "))
except:
    print('Valor inválido!')
    print('Use somente números em casas decimais entre 0 e 1')
    quit()

print(calcula_nota(nota))