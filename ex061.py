#61

def soma(*numeros):
    final = 0
    for x in numeros:
        final += x
    print(f"O resultado final é: {final}")
    
soma(12,34,54,76)