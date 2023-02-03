import sqlite3
from view import View
from model import Model
from controller import Controller

# Criar conexão com o banco de dados
conn = sqlite3.connect('finances.db')

# Instanciar o modelo
model = Model(conn)

# Instanciar a visão
view = View()

# Instanciar o controlador
controller = Controller(model, view)

# Iniciar a aplicação
controller.start()

# Fechar a conexão com o banco de dados
conn.close()
