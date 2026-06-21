from datetime import datetime
from Entradas_Mundial.models import db

class Compra(db.Model):
    __tablename__ = 'compras'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow) 
    total_pagado = db.Column(db.Float, nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)
    estado_pago = db.Column(db.String(20), default='pendiente', nullable=False)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios_cliente.id'), nullable=False) 
    
    # Relación corregida para asegurar borrado en cascada
    entradas_asociadas = db.relationship('Entrada', backref='compra_rel', lazy=True, cascade="all, delete-orphan") 
    
    def crear_transaccion(self):
        pass
    
    def calcular_total(self):
        return sum(entrada.precio for entrada in self.entradas_asociadas)
    
    def procesar_pago(self):
        self.estado_pago = 'completado'
        db.session.commit()