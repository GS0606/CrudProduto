
import sqlite3

class Dbprodutos:

    def __init__(self, nome_banco='loja_virtual5.db'):
        
        self.nome_banco = nome_banco
        
    def conectar(self):
        
        self.conexao = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexao.cursor()
        
    def desconectar(self):
        
        self.conexao.close()
    
    def criar_tb(self):
        
        self.conectar()
        self.cursor.execute("CREATE TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor INTEGER)")

        self.conexao.commit()
        self.desconectar()
    
    
teste = Dbprodutos()
teste.criar_tb()
  
        

        
    