'''Documentação:
https://www.youtube.com/watch?v=yZ83sZUvLVw
Programação Orientação a objetos(POO) é um paradigma de programação que contem 4 pilares.
POO tende a levar algo do mundo real para o computador.

1- Propriedade Abstração
Classe será a definição do objeto, por exemplo uma cenaca que possuia as "propriedades" de cor, logo e tamanho, e suas funcionalidades podem ser a de beber e encher.

Classe é o molde do obejto, a abstração geral do objeto, a denifição geral, pode-se existir objetos com definições iguais, porem diferentes, como por exemplo a cor de duas canecas diferentes.

-----A Classe é o molde para se fazer um objeto. -----

2- Herança

Pode-se existir classes pais e classes filhas, as classes filhas são provenientes das classes pais, classes filhas herdam os propriedades e os métodos das clases pais.

3 - Polimorfismo

Polimorfismo é a capacidade de resscrever ou sobescrever métodos da classe pai. basicamente uma classe filha executando um método da forma dela.

4 - Encapsulamento
Linguagens de programação como java e c# se usa o public e o private, no entanto no python não existe isso.

No python, para se falar que é uma propriedade privada, se coloca dois anderlines antes do nome '__teste', no entanto isso é hackiavel.

Quando é utilizado o  '__' o python muda o nome do atributo para o _nome da classe + __Nome do atributo privado, dessa forma é possivel acessar um atributo mesmo ele sendo privado.
Exemplo:
       Nome do obj._NomeClasse__NomeAtributo
print(caneca_bylearn._Caneca__preco_fabrica)

Exemplo 2:
caneca_bylearn._Caneca__preco_fabrica = 1

Uma forma de fazer o emcapsulamento de forma mais segura é com properts onde o método seter é modificado.
'''


#A Classe é o molde para se fazer um objeto.
class Caneca:
    formato = 'Cilindrico com alça lateral' #Propriedade estática da classe que em todo obj será o mesmo

    #__init__ é o contrutor que Cria propriedades obrigatórias que vão variar em cada obj
    def __init__(self, nome, logo, cor):#self indica em especifico qual é o objeto que está chamando a função
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'
        self.preco = 25.99 #as classes filhas herdam esse tipo de propriedade, para alterar o seu valor em  cada classe deve-se alterar no construtor da classe filha.

        self.__preco_fabrica = 15 #Propriedade privada devido os '__'
        #Propriedades do objeto
    
    def beber(self):
        self.status = 'Vazia'
        return f'É da {self.nome} que eu estou bebendo.'
    
    def encher(self):
        self.status = 'Cheia'
        return f'Estou enchendo a {self.nome}'

#Herança: Classe filha da classe pai Caneca.
class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__('Caneca Londrina', 'Cidade de londres', 'Branca') 
        
        #super significa que será utilizado o construtor da classe super(pai), assim não sendo necessário refazes os códigos a baixo:
        '''self.nome = 'Caneca Londrina'
        self.logo = 'Cidade de londres'
        self.cor = 'Branca'
        self.status = 'Cheia'''
        
        self.bebida = 'Chá' #Propriedade unica da classe para fazer o Polimorfismo
        self.preco = 30.00
    #métodos beber e encher foram herdados da classe pai

    #método somenta dessa classe filha, a classe pai não tem acesso a ele.
    def extras(self):
        print('Como bonos você ganha uma colher.')
    
    #Polimorfismo: reescrevendo método original para esse obj
    def beber(self):
        self.status = 'Vazia'
        return f'Está na hora do chá das 5.'

class CanecaBatman(Caneca):
    def __init__(self):
        super().__init__('Caneca Gothan', 'Batman', 'preta') 
        self.bebida = 'café'
        self.preco = 34.90

    def som(self):
        print('I m Batman')

    def beber(self):
        #Polimorfismo: Ultiliza o método original mas com uma pequena alteração
        return super().beber() + f' {self.bebida}'

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