from datetime import datetime
from Entradas_Mundial.models import db

class Compra(db.Model):
    __tablename__ = 'compras'
    id = db.Column(db.Integer, primary_key=True)
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow) # <-- Corregido 'fecha_comptra'
    total_pagado = db.Column(db.Float, nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)
    estado_pago = db.Column(db.String(20), nullable=False)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False) # <-- Corregido 'usuari_id'
    entradas_asociadas = db.relationship('Entrada', backref='compra', lazy=True) # <-- Corregido 'entadas_asociadas'
    
    def crear_transaccion(self):
        pass
    
    def calcular_total(self):
        pass
    
    def procesar_pago(self):
        pass
    
    
