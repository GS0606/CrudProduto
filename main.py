from exercicio import CRUD

class Produto:
    def __init__(self,id,nome,preco):
        
        self.id = id
        self.nome = nome
        self.preco = preco
        
class Funcao:
    def __init__(self):
        self.produto = []
        
    def criar_produto(self,id,nome,preco):
        