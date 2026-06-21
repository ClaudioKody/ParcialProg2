from flask_login import UserMixin
from Entradas_Mundial.models import db

class UsuarioBase(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    _password = db.Column('password', db.String(255), nullable=False) # Aumentado a 255 para hashes
    
    __mapper_args__ = {
        'polymorphic_on': rol,
        'polymorphic_identity': 'base'
    }

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, nueva_password):
        if len(nueva_password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        self._password = nueva_password
    
    @property
    def es_admin(self):
        return self.rol == 'administrador'

class UsuarioCliente(UsuarioBase):
    __tablename__ = 'usuarios_cliente'
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    tarjeta_credito_asociada = db.Column(db.String(20), nullable=True)
    
    # Relación con compras
    compras = db.relationship("Compra", backref="usuario_cliente", lazy=True, cascade="all, delete-orphan")
    
    __mapper_args__ = {'polymorphic_identity': 'cliente'}

class Administrador(UsuarioBase):
    __tablename__ = 'administradores'
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    dni = db.Column(db.String(50), unique=True, nullable=False)
    
    __mapper_args__ = {'polymorphic_identity': 'administrador'}