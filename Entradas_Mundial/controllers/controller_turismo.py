from flask import render_template, session, abort, redirect, url_for, flash
from Entradas_Mundial.models.model_actividad_turistica import Concierto, ActividadRecreativa, ActividadTuristica

def mostrar_actividades_sede():
    datos_ticket = session.get('ticket_exitoso')
    
    if not datos_ticket:
        return render_template('turismo/sin_acceso.html') 
        
    ciudad_sede = datos_ticket['ciudad']

    # Filtramos por ciudad (no por ubicacion, que es el nombre del estadio/lugar)
    conciertos_locales = Concierto.query.filter_by(ciudad=ciudad_sede).all()
    recreaciones_locales = ActividadRecreativa.query.filter_by(ciudad=ciudad_sede).all()
    
    return render_template(
        'turismo/ver_actividades.html', 
        ciudad=ciudad_sede,
        conciertos=conciertos_locales, 
        recreaciones=recreaciones_locales
    )

# NUEVO: función para mostrar el detalle de una actividad por su id
def detalle_actividad(id):
    # Busca en la tabla base (polimórfica), devuelve el objeto real (Concierto o ActividadRecreativa)
    actividad = ActividadTuristica.query.get_or_404(id)
    return render_template('turismo/detalles_actividades.html', actividad=actividad)

def reservar_actividad(id):
    actividad = ActividadTuristica.query.get_or_404(id)

    flash(f'¡La actividad "{actividad.nombre}" fue reservada con éxito!', 'success')

    return redirect(url_for('routes_turismo.detalle_actividad', id=id))