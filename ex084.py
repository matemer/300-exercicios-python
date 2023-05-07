def msg():
    global mensagem
    print(mensagem)
    mensagem = 'Mensagem global'
    print(mensagem)

mensagem = 'Olá, seja bem vindo!'

msg()