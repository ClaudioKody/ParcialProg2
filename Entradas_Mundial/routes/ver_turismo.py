from flask import Blueprint, render_template
from Entradas_Mundial.controllers import controller_turismo
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_turismo = Blueprint('routes_turismo', __name__)

@routes_turismo.route('/turismo/recomendaciones')
@login_requerido
def mostrar_actividades_sede():
    return controller_turismo.mostrar_actividades_sede()

# NUEVO: ruta para el detalle de cada actividad
@routes_turismo.route('/turismo/detalle/<int:id>')
@login_requerido
def detalle_actividad(id):
    return controller_turismo.detalle_actividad(id)

@routes_turismo.route('/turismo/reservar/<int:id>')
@login_requerido
def reservar_actividad(id):
    return controller_turismo.reservar_actividad(id)