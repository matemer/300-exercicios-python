#080

def morse(valor):
    dic = {'A':'.....',
           'B':'.--.-',
           'C':'.-.-',
           'D':'...--',
           'E':'--.-.'}

    return ''.join(dic[i] for i in valor.upper())

valor = 'abc'

conversor = morse(valor)

print(conversor)