from Entradas_Mundial import db

class ActividadTuristica(db.Model):
    __tablename__='actividades_turisticas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    precio_sugerido = db.Column(db.Float, nullable=True)
    imagen_url = db.Column(db.String(255), nullable=True)
    tipo_actividad = db.Column(db.String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_on': tipo_actividad
    }

    def info_general_evento(self):
        pass
    
    def mostrar_recomendacion(self):
        return f"Recomendacion general para {self.ciudad}"
    
class Concierto(ActividadTuristica):
    __tablename__ = 'conciertos'
    id = db.Column(db.Integer, db.ForeignKey('actividades_turisticas.id'), primary_key=True)

    artista = db.Column(db.String(100), nullable=True)
    estadio_recital = db.Column(db.String(100), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'concierto'
    }

    def mostrar_recomendacion(self):
        return f"¡No te pierdas a {self.artista} en el {self.estadio_recital}!"
    
class ActividadRecreativa(ActividadTuristica):
    __tablename__ = 'actividades_recreativas'
    id = db.Column(db.Integer, db.ForeignKey('actividades_turisticas.id'), primary_key=True)
    
    horarios_disponibles = db.Column(db.String(255), nullable=True)
    direccion_establecimiento = db.Column(db.String(255), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'actividad_recreativa'
    }

    def mostrar_recomendacion(self):
        return f"Visita este lugar en {self.direccion_establecimiento}. Horarios: {self.horarios_disponibles}"
    