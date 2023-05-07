#83

import random

tamanho = int(input("Qual o tamanho do password? "))

s = 'qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM123456789!@#$%*()'

senha = ''.join(random.sample(s,tamanho))

print(senha)