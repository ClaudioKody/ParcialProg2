import uuid
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_required
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada

@login_required
def procesar_compra_pasos(id_partido):
    partido = Partido.query.get_or_404(id_partido)
    
    if request.method == 'POST':
        # Datos del asistente
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        dni = request.form.get('dni')
        nacionalidad = request.form.get('nacionalidad')
        categoria = request.form.get('categoria_asiento')
        asiento = request.form.get('numero_asiento')
        
        # Lógica de precios
        monto_total = partido.precio_base
        if request.form.get('hospitality') == 'on': monto_total += 75
        if request.form.get('estacionamiento') == 'on': monto_total += 30
        
        # Validar disponibilidad
        if not partido.verificar_disponibilidad():
            flash('Lo sentimos, no hay disponibilidad para este partido.', 'danger')
            return redirect(url_for('routes_partidos.lista_partidos'))
            
        # 1. Crear Compra
        nueva_compra = Compra(
            usuario_id=current_user.id,
            total_pagado=monto_total,
            metodo_pago="Tarjeta",
            estado_pago="completado"
        )
        db.session.add(nueva_compra)
        db.session.flush() # Obtener ID antes de commitear

        # 2. Crear Entrada
        codigo = str(uuid.uuid4()).upper()[:10]
        nueva_entrada = Entrada(
            nombre_asistente=nombre,
            apellido_asistente=apellido,
            email_asistente=email,
            documento_asistente=dni,
            nacionalidad_asistente=nacionalidad,
            categoria_asiento=categoria,
            numero_asiento=asiento,
            codigo_acceso=codigo,
            compra_id=nueva_compra.id,
            partido_id=partido.id
        )
        
        # 3. Actualizar disponibilidad
        partido.capacidad_disponible -= 1
        
        db.session.add(nueva_entrada)
        db.session.commit()

        # Guardar en sesión para mostrar en confirmación
        session['ticket_exitoso'] = {
            'titular': f"{nombre} {apellido}",
            'partido': f"{partido.equipo1} vs {partido.equipo2}",
            'categoria': categoria,
            'asiento': asiento,
            'total': monto_total,
            'codigo': codigo
        }
        
        return redirect(url_for('routes_compras.confirmacion'))

    return render_template('compra/seleccionar_asiento.html', partido=partido)

def mostrar_confirmacion():
    datos_ticket = session.get('ticket_exitoso')
    if not datos_ticket:
        return redirect(url_for('routes_partidos.lista_partidos'))
    return render_template('compra/confirmacion.html', ticket=datos_ticket)