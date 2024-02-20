import sqlite3

banco = sqlite3.connect('loja_virtual.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor INTEGER)")

# CRIAR
cursor.execute("INSERT INTO produtos VALUES('1','bOLO','25')")
banco.commit()

#  LER
cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())

# EDITAR
# cursor.execute("UPDATE produtos SET valor = 10 WHERE nome = 'Café'")
# banco.commit()

#EXCLUIR
# cursor.execute("DELETE FROM produtos WHERE id = 1")
# banco.commit()