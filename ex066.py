#66

numeros = [1,2,3,5]

dados = ['Hello', 'Whats up', 'Everything good?']

def morethanone(*args,**args2):
    print(args)
    print(args2)
    
morethanone(numeros,dados)