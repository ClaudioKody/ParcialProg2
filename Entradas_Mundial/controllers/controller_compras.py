import uuid
from flask import render_template, request, redirect, url_for, flash, session
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada

# PASO 2: Selección de ubicación y cantidad de tickets
def procesar_seleccion_asientos(id_partido):
    partido = Partido.query.get_or_404(id_partido)
    # CORREGIDO: Redirección al archivo HTML del paso 2 que creamos
    return render_template('partidos/seleccionar_asientos.html', partido=partido)

# PASO 3: Formulario para ingresar DNI, nombres y procesar lógica de base de datos
def procesar_datos_comprador():
    return render_template('partidos/datos_comprador.html')

# PASO 4: Pasarela de pago simulada con tarjeta de crédito
def procesar_pago_tarjeta():
    return render_template('partidos/pago.html')

# PASO 5: Muestra la pantalla de éxito final
def mostrar_confirmacion():
    datos_ticket = session.get('ticket_exitoso')
    if not datos_ticket:
        # CORREGIDO: Sincronizado a la ruta correcta si falla la sesión
        return redirect(url_for('routes_partidos.lista_partidos'))
    
    # CORREGIDO: Apunta de manera exacta a partidos/confirmacion.html
    return render_template('partidos/confirmacion.html', ticket=datos_ticket)

# FUNCIÓN ANTERIOR INTEGRADA: Mantiene viva la lógica interna que crearon tus compañeros
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
            return redirect(url_for('routes_partidos.lista_partidos'))
            
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
        
        return redirect(url_for('routes_compras.confirmacion'))

    return render_template('partidos/seleccionar_asientos.html', partido=partido)