
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
    
    def inserir_produto(self, nome , valor):
        
        self.conectar()
        self.cursor.execute("INSERT INTO produtos (nome, valor) VALUES (?, ?)", (nome, valor))
        
        self.conexao.commit()
        self.desconectar()
    
    def listar_produto(self):
        
        self.conectar()
        self.cursor.execute("SELECT * FROM produtos")
        produtos = self.cursor.fetchall()
        self.conexao.commit()
        self.desconectar()
        return produtos
    
    def atualizar_produto(self, id, nome, valor):
        self.conectar()
        self.cursor.execute("UPDATE produtos SET nome=?, valor=? WHERE id= ?",(nome, valor, id) )
        self.conexao.commit()
        self.desconectar()
        
        
    def deletar_produto(self, id):
        self.conectar()
        self.cursor.execute("DELETE FROM produtos WHERE id=?", (id,))
        self.conexao.commit()
        self.desconectar()
    
teste = Dbprodutos()


# teste.criar_tb()


# teste.inserir_produto("CIMENTO" ,61)

produtos = teste.listar_produto()
print("Lista de Produto:  ")
for produto in produtos:
    print(produto)


# id_produto = 1
# teste.atualizar_produto(id_produto, "BALDE", 29 )

# produtos_atualizados = teste.listar_produto()
# print("\nLista de produtos atualizados:")
# for produto in produtos_atualizados:
#     print(produto)
        
        
# remover_id = 10
# teste.deletar_produto(remover_id)
# print(f"\nProduto com ID {remover_id} deletado.")


    