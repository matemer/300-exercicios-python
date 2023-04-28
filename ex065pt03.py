'''65 - Aprimore o exemplo anterior, incluindo um módulo simulando o cadastro de usuários em um plano de saúde, apenas permitindo
o agendamento de consulta caso o usuário que esta interagindo com o programa conste no cadastro'''

import ex065pt01 as ex1
import ex065pt02 as ex2

usuario = input("Digite seu número de usuário: ")

if usuario in ex2.clientes.keys():
    med = input(f"Seja bem vindo! Com qual médico deseja se consultar? {ex1.medicos}")
    
    if med in ex1.medicos:
        print("Consulta marcada!")
    
else:
    print("Este usuário não esta na nossa base, por favor tente novamente.")
    breakpoint