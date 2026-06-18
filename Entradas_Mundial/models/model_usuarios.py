from flask import Blueprint
from Entradas_Mundial.models import db

class UsuarioBase(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    rol = db.Column(db.String(50), nullable=False)
    
    _password = db.Column('password', db.String(255), nullable=False)
    
    __mapper_args__ = {
        'polymorphic_on': 'rol'
    }
    
    @property
    def password(self):
        """ Getter: Permite leer la contraseña de forma controlada """
        return self._password
    
    @password.setter
    def password(self, nueva_password):
        """ Setter: Aplica una regla de validación antes de guardar el dato """
        if len(nueva_password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres por seguridad.")
        self._password = nueva_password
        
    def iniciar_sesion(self):
        pass
    
    def cerrar_sesion(self):
        pass
    
    def editar_password(self):
        pass
    

class UsuarioCliente(UsuarioBase):
    __tablename__ = 'usuarios_cliente'
    
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'cliente'
    }
    
    compras = db.relationship("Compra", backref="cliente", lazy=True)

    def bucar_partidos(self):
        pass

    def seleccionar_partido(self):
        pass

    def comprar_entradas(self):
        pass


class Administrador(UsuarioBase):
    __tablename__ = 'administradores'
    
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    dni = db.Column(db.String(50), unique=True, nullable=False)
    
    __mapper_args__ = {
        'polymorphic_identity': 'administrador'
    }
    
    def visualizar_general(self):
        pass

    def editar_datos(self):
        pass

    def editar_datos_permitidos(self):
        pass