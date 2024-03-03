from flask import Flask, jsonify, request

app = Flask(__name__)


produtos =  [
    {
        'id': 1,
        'nome': 'Carrinho de mão',
        'preco': 70
    },
    {
        'id': 2,
        'nome': 'Balde',
        'preco': 20
    },
      {
        'id': 3,
        'nome': 'Cimento',
        'preco': 75
    }
    
]
@app.route('/produtos',methods=['GET'])
def buscar_produto():
    return jsonify(produtos)

@app.route('/produtos/<int:id>',methods=['GET'])
def buscar_produto_id(id):
    for produto in produtos:
       if produto.get('id') == id:
           return jsonify(produto)
       
@app.route('/produtos/<int:id>',methods= ['PUT'])
def editar_produto_id(id):
    produto_alterado= request.get_json()
    for indice,produto in enumerate(produtos):
        if produto.get('id')== id:
            produtos[indice].update(produto_alterado)
            return jsonify(produtos[indice])

@app.route('/produtos',methods=['POST'])
def inserir_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    
    return jsonify(produtos)

@app.route('/produtos/<int:id>',methods= ['DELETE'])
def excluir_produto(id):
    for indice,produto in enumerate(produtos):
        if produto.get('id') == id:
            del produtos[indice]
            
    return jsonify(produtos)
    
app.run(port=5000,host='localhost',debug=True)