import ex064pt01 as ex

escolha = input(f"Digite o nome do médico que deseja realizar a consulta: {ex.med}")

if escolha == ex.med[0]:
    print(f"Sua consulta foi agendada com o médico: {ex.med[0]}")

elif escolha == ex.med[1]:
    print(f"Sua consulta foi agendada com o médico: {ex.med[1]}")

elif escolha == ex.med[2]:
    print(f"Sua consulta foi agendada com o médico: {ex.med[2]}")

else:
    print("Você digitou errado!")