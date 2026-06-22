from Entradas_Mundial.models import db

class Entrada(db.Model):
    __tablename__ = 'entradas' 
    
    id = db.Column(db.Integer, primary_key=True) 
    nombre_asistente = db.Column(db.String(100), nullable=False)
    apellido_asistente = db.Column(db.String(100), nullable=False)
    email_asistente = db.Column(db.String(100), nullable=False)
    documento_asistente = db.Column(db.String(20), nullable=False)
    nacionalidad_asistente = db.Column(db.String(50), nullable=False)
    categoria_asiento = db.Column(db.String(20), nullable=False)
    numero_asiento = db.Column(db.String(10), nullable=False)
    codigo_acceso = db.Column(db.String(50), unique=True, nullable=False) 
    
    compra_id = db.Column(db.Integer, db.ForeignKey('compras.id'), nullable=False) 
    partido_id = db.Column(db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    
    def registrar_asistente(self):
        pass
    
    def generar_codigo_acceso(self):
        import uuid
        return str(uuid.uuid4()).upper()[:10]
    
    def enviar_email_confirmacion(self):
        pass