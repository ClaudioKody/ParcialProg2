import uuid
import qrcode
import io
import base64
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_required
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada

@login_required
def seleccionar_asientos(id_partido):
    partido = Partido.query.get_or_404(id_partido)
    if request.method == 'POST':

        categoria = request.form.get('categoria')
        cantidad = request.form.get('cantidad')
        
        session['pre_compra'] = {
            'id_partido': id_partido,
            'categoria': categoria,
            'cantidad': cantidad
        }
        session.modified = True
        return redirect(url_for('routes_compras.datos_comprador'))
    return render_template('compra/seleccionar_asientos.html', partido=partido)

@login_required
def datos_comprador():
    if 'pre_compra' not in session:
        flash("Por favor, selecciona los asientos primero.", "warning")
        return redirect(url_for('routes_partidos.lista_partidos'))
    return render_template('compra/datos_comprador.html')

@login_required
def procesar_compra_final():
    pre_compra = session.get('pre_compra')
    if not pre_compra:
        return redirect(url_for('routes_partidos.lista_partidos'))
        
    partido = Partido.query.get_or_404(pre_compra['id_partido'])
    
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email')
    dni = request.form.get('dni')
    nacionalidad = request.form.get('nacionalidad')
    numero_asiento = request.form.get('numero_asiento')
    
    monto_total = partido.precio_base * int(pre_compra['cantidad'])
    
    nueva_compra = Compra(
        usuario_id=current_user.id,
        total_pagado=monto_total,
        metodo_pago="Tarjeta",
        estado_pago="completado"
    )
    db.session.add(nueva_compra)
    db.session.flush() 

    codigo = str(uuid.uuid4()).upper()[:10]
    nueva_entrada = Entrada(
        nombre_asistente=nombre,
        apellido_asistente=apellido,
        email_asistente=email,
        documento_asistente=dni,
        nacionalidad_asistente=nacionalidad,
        numero_asiento=numero_asiento,
        categoria_asiento=pre_compra['categoria'],
        compra_id=nueva_compra.id,
        partido_id=partido.id,
        codigo_acceso=codigo
    )
    
    partido.capacidad_disponible -= int(pre_compra['cantidad'])
    db.session.add(nueva_entrada)
    db.session.commit()

    session.pop('pre_compra', None)
    session['ticket_exitoso'] = {
        'titular': f"{nombre} {apellido}", 
        'codigo': codigo, 
        'ciudad': partido.ciudad,
        'partido': f"{partido.equipo1} vs {partido.equipo2}"
    }
    
    return redirect(url_for('routes_compras.confirmacion', id_entrada=nueva_entrada.id))

@login_required
def mostrar_confirmacion(id_entrada):
    entrada = Entrada.query.get_or_404(id_entrada)
    qr_code = generar_qr_base64(entrada.codigo_acceso)
    return render_template('compra/confirmacion.html', entrada=entrada, qr_code=qr_code)

def generar_qr_base64(data):
    qr = qrcode.make(data)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode('utf-8')