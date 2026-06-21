from Entradas_Mundial.models import db

class Partido(db.Model):
    __tablename__ = 'partidos'
    
    id = db.Column(db.Integer, primary_key=True)
    equipo1 = db.Column(db.String(50), nullable=False)
    equipo2 = db.Column(db.String(50), nullable=False)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    estadio = db.Column(db.String(100), nullable=False)
    capacidad_estadio = db.Column(db.Integer, nullable=False)
    capacidad_disponible = db.Column(db.Integer, nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    fase = db.Column(db.String(50), nullable=False)
    precio_base = db.Column(db.Float, nullable=False)
    
    # Relación con borrado en cascada
    entradas = db.relationship('Entrada', backref='partido_rel', lazy=True, cascade="all, delete-orphan")
    
    def obtener_detalles(self):
        return f"{self.equipo1} vs {self.equipo2} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M')} en {self.estadio}, {self.ciudad} ({self.fase})"
    
    def verificar_disponibilidad(self):
        return self.capacidad_disponible > 0