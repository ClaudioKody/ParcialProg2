from flask import render_template, session
from Entradas_Mundial.models.model_actividad_turistica import Concierto, ActividadRecreativa

def mostrar_actividades_sede():
    datos_ticket = session.get('ticket_exitoso')
    if not datos_ticket:
        return "Para ver las actividades primero debés adquirir un ticket.", 400
        
    ciudad_sede = datos_ticket['ciudad']
    
    conciertos_locales = Concierto.query.filter_by(ubicacion=ciudad_sede).all()
    recreaciones_locales = ActividadRecreativa.query.filter_by(ubicacion=ciudad_sede).all()
    
    return render_template(
        'turismo_recomendaciones.html', 
        ciudad=ciudad_sede,
        conciertos=conciertos_locales, 
        recreaciones=recreaciones_locales
    )