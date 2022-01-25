#A Classe é o molde para se fazer um objeto.
class Caneca:
    
    formato = 'Cilindrico com alça lateral'  #Atributo estático em todo objeto 

    #Construtor
    def __init__(self, nome, logo, cor): #Parametros para os atributos
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'
        self.preco = 25.99 
        self.__preco_fabrica = 15 
    
    def beber(self):
        self.status = 'Vazia'
        return f'É da {self.nome} que eu estou bebendo.'
    
    def encher(self):
        self.status = 'Cheia'
        return f'Estou enchendo a {self.nome}'