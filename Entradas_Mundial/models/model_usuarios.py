from flask_login import UserMixin
from Entradas_Mundial.models import db


class UsuarioBase(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    rol = db.Column(db.String(50), nullable=False)
    
 
    _password = db.Column('password', db.String(50), nullable=False)

    
    __mapper_args__ = {
        'polymorphic_on': 'rol'
    }

    # --- MÉTODOS REQUERIDOS POR FLASK-LOGIN ---
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    # ------------------------------------------

    @property
    def es_admin(self):
        return self.rol == 'administrador'
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, nueva_password):
        if len(nueva_password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres por seguridad.")
        self._password = nueva_password
        
    def iniciar_sesion(self):
        pass
    
    def cerrar_sesion(self):
        pass
    
    def editar_password(self):
        pass

# ... (El resto de tus clases UsuarioCliente y Administrador se mantienen IGUAL) ...

class UsuarioCliente(UsuarioBase):
    __tablename__ = 'usuarios_cliente'
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'cliente'}
    compras = db.relationship("Compra", backref="cliente", lazy=True)
    tarjeta_credito_asociada = db.Column(db.String(20), nullable=True)


class Administrador(UsuarioBase):
    __tablename__ = 'administradores'
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    dni = db.Column(db.String(50), unique=True, nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'administrador'}