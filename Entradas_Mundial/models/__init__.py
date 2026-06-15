from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from .model_usuarios import UsuarioBase, UsuarioCliente, Administrador
from .model_partido import Partido
from .model_compra import Compra
from .model_entradas import Entrada
