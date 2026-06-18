from Entradas_Mundial.models import db

class UsuarioBase(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    
    __mapper_args__ = {
        'polymorphic_on': rol
    }
    
    def iniciar_sesion(self):
        pass
    
    def cerrar_sesion(self):
        pass
    
    def editar_password(self):
        pass
    
class UsuarioCliente(UsuarioBase): # <-- CORREGIDO: Ahora hereda de UsuarioBase
    __tablename__ = 'usuarios_cliente'
    
    id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'cliente'
    }
    
    # Esta relación buscará la clave foránea en la tabla 'compras'
    compras = db.relationship("Compra", backref="cliente", lazy=True)

    def bucar_partidos(self):
        pass

    def seleccionar_partido(self):
        pass

    def comprar_entradas(self):
        pass

class Administrador(UsuarioBase): # <-- CORREGIDO: Ahora hereda de UsuarioBase
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