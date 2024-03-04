from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect('loja_virtual10.db')

@app.route('/produtos', methods=['GET'])
def buscar_produtos():
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()
    conexao.close()
    return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_produto_por_id(id):
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto WHERE id=?", (id,))
    produto = cursor.fetchone()
    conexao.close()
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"mensagem": "Produto não encontrado"}), 404

@app.route('/produtos', methods=['POST'])
def inserir_produto():
    novo_produto = request.get_json()
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produto (nome, valor) VALUES (?, ?)", (novo_produto['nome'], novo_produto['valor']))
    conexao.commit()
    conexao.close()
    return jsonify({"mensagem": "Produto inserido com sucesso"})

@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_produto(id):
    produto_alterado = request.get_json()
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET nome=?, valor=? WHERE id=?", (produto_alterado['nome'], produto_alterado['valor'], id))
    conexao.commit()
    conexao.close()
    return jsonify({"mensagem": "Produto atualizado com sucesso"})

@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produto WHERE id=?", (id,))
    conexao.commit()
    conexao.close()
    return jsonify({"mensagem": "Produto excluído com sucesso"})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
