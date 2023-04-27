#62

def identificacao(*args,**kwargs):
    for n in args:
        nome = n
        
    for k,v in kwargs.items():
        idade = k
        sexo = v
        
        print(f'Nome: {nome}, {idade}, {sexo}')
        
pessoa = identificacao('Fernando', idade = 33, sexo = 'M')