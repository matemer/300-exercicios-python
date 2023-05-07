#69

class Carro:
    ano = 2012
    cor = 'Preto'
    modelo = 'Menor'

carro1 = Carro()

carro2 = Carro()

carro2.ano = 2013
carro2.cor = 'Rosa'
carro2.modelo = 'Maior'

print(carro1.ano, carro1.cor, carro1.modelo)
print(carro2.ano,carro2.cor, carro2.modelo)