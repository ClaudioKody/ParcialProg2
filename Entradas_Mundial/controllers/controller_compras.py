import uuid
from flask import render_template, request, redirect, url_for, flash, session
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada

def procesar_compra_pasos(id_partido):
    partido = Partido.query.get_or_404(id_partido)
    
    if request.method == 'POST':
        nombre_titular = request.form.get('nombre')
        apellido_titular = request.form.get('apellido')
        dni_titular = request.form.get('dni')
        email_titular = request.form.get('email')
        categoria_asiento = request.form.get('categoria_asiento')
        monto_total = partido.precio_base
        adicionales_precio = 0
        
        if request.form.get('hospitality') == 'on': adicionales_precio += 75
        if request.form.get('estacionamiento') == 'on': adicionales_precio += 30
        if request.form.get('kit_bienvenida') == 'on': adicionales_precio += 45
        
        monto_total += adicionales_precio

        if partido.capacidad_disponible <= 0:
            flash('Lo sentimos, ya no quedan entradas disponibles para este partido.', 'danger')
            return redirect(url_for('inicio_partidos'))
        nueva_compra = Compra(
            usuario_id=session.get('user_id'),
            monto_total=monto_total,
            metodo_pago="Tarjeta de Crédito/Débito"
        )
        db.session.add(nueva_compra)
        db.session.flush()

        codigo_confirmacion = str(uuid.uuid4()).upper()[:10]

        nueva_entrada = Entrada(
            partido_id=partido.id,
            compra_id=nueva_compra.id,
            categoria=categoria_asiento,
            precio=monto_total,
            codigo_acceso=codigo_confirmacion 
        )
        
        partido.capacidad_disponible -= 1
        
        db.session.add(nueva_entrada)
        db.session.commit()

        session['ticket_exitoso'] = {
            'titular': f"{nombre_titular} {apellido_titular}",
            'dni': dni_titular,
            'email': email_titular,
            'partido': f"{partido.pais_local} vs {partido.pais_visitante}",
            'estadio': partido.estadio,
            'ciudad': partido.ciudad,
            'categoria': categoria_asiento,
            'total': monto_total,
            'codigo_confirmacion': codigo_confirmacion
        }
        
        return redirect(url_for('confirmacion_ticket'))

    return render_template('compra_formulario.html', partido=partido)

def mostrar_confirmacion():
    datos_ticket = session.get('ticket_exitoso')
    if not datos_ticket:
        return redirect(url_for('inicio_partidos'))
    
    return render_template('confirmacion.html', ticket=datos_ticket)