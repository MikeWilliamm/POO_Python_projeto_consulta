from canecas.caneca import Caneca


class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__('Caneca Londrina', 'Cidade de londres', 'Branca') 
        
        self.bebida = 'Chá'
        self.preco = 30.00

    def extras(self):
        print('Como bonos você ganha uma colher.')
    
    def beber(self):
        self.status = 'Vazia'
        return f'Está na hora do chá das 5.'