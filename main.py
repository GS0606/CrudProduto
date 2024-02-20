from exercicio import CRUD

class Produto:
    def __init__(self,id,nome,preco):
        
        self.id = id
        self.nome = nome
        self.preco = preco
        
class FuncaoCrud:
    def __init__(self):
        self.produtos = []
        
    def criar_produto(self,id,nome,preco):
        
        produto = Produto()
        self.produto.append()
        return produto
    
    def listar_produto(self):
        
        return self.produtos 
     
    def buscar_produto(self, id):
         
         for produto in self.produtos:
            if produto.id == id:
                return produto
         return None
    
    def alterar_produto(self,id,nome,preco):
        
        produto = self.buscar_produto(id)
        if produto:
            produto.nome = nome
            produto.preco = preco
            return True
        else:
            
            return False
        
    