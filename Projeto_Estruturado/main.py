from canecas.caneca import Caneca
from canecas.caneca_londres import *
from canecas.caneca_batman import *

#Instanciando OBJETOS    
caneca_londres = CanecaLondrina()
caneca_bylearn = Caneca('Caneca ByLearner', 'Foguete', 'Branca')
caneca_batman = CanecaBatman()

print('-'*42)
print(f'A caneca {caneca_londres.nome} possui a logo {caneca_londres.logo}.')
print(f'A caneca {caneca_bylearn.nome} possui a logo {caneca_bylearn.logo}.')
print(f'A caneca {caneca_batman.nome} possui a logo {caneca_batman.logo}.')
print('-'*42)
print(caneca_londres.beber())
print(caneca_londres.encher())
print(caneca_bylearn.beber())
print(caneca_batman.beber())
print('-'*42)
print(f'caneca_londes: {caneca_londres.status}')
print(f'caneca_bylearn: {caneca_bylearn.status}')
print(f'caneca_batman: {caneca_batman.status}')
print('-'*42)
caneca_londres.extras()
caneca_batman.som()
print('-'*42)
print('----- Promoção -----')
caneca_batman.preco = caneca_batman.preco - 5
caneca_londres.preco = caneca_londres.preco - 5
caneca_bylearn.preco = caneca_bylearn.preco - 5

print('----- NOVOS PRECOS -----')
print(f'A caneca {caneca_batman.nome} tem o preco de {caneca_batman.preco} reais')
print(f'A caneca {caneca_londres.nome} tem o preco de {caneca_londres.preco} reais')
print(f'A caneca {caneca_bylearn.nome} tem o preco de {caneca_bylearn.preco} reais')

print('-'*42)
print(caneca_bylearn._Caneca__preco_fabrica)
caneca_bylearn._Caneca__preco_fabrica = 1
print(caneca_bylearn._Caneca__preco_fabrica)