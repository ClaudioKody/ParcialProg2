from datetime import datetime
from Entradas_Mundial.models import db

class Compra(db.Model):
    __tablename__ = 'compras'
    id=db.Column(db.Integer, primary_key=True)
    fecha_comptra=db.Column(db.DateTime, default=datetime.utcnow)
    total_pagado=db.Column(db.Float, nullable=False)
    metodo_pago=db.Column(db.String(50), nullable=False)
    estado_pago= db.Column(db.String(20), nullable=False)
    
    usuari_id=db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    entadas_asociadas=db.relationship('Entrada', backref='compra', lazy=True)
    
    def crear_transaccion(self):
        pass
    
    def calcular_total(self):
        pass
    
    def procesar_pago(self):
        pass
    
    
