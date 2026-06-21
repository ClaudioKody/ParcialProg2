from flask import render_template, session
from Entradas_Mundial.models.model_actividad_turistica import Concierto, ActividadRecreativa

def mostrar_actividades_sede():
    # Verificamos si el usuario tiene un ticket en la sesión
    datos_ticket = session.get('ticket_exitoso')
    if not datos_ticket:
        return "Para ver las actividades primero debés adquirir un ticket.", 400
        
    ciudad_sede = datos_ticket['ciudad']
    
    # Obtenemos las actividades filtradas por la ciudad del ticket
    conciertos_locales = Concierto.query.filter_by(ubicacion=ciudad_sede).all()
    recreaciones_locales = ActividadRecreativa.query.filter_by(ubicacion=ciudad_sede).all()
    
    # RUTA ACTUALIZADA: Apuntamos a la subcarpeta turismo/
    return render_template(
        'turismo/ver_actividades.html', 
        ciudad=ciudad_sede,
        conciertos=conciertos_locales, 
        recreaciones=recreaciones_locales
    )