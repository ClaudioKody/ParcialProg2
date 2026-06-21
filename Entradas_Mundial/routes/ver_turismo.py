from flask import Blueprint , render_template
from Entradas_Mundial.controllers import controller_turismo
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_turismo = Blueprint('routes_turismo', __name__)

@routes_turismo.route('/turismo/recomendaciones')
@login_requerido
def mostrar_actividades_sede():
    return controller_turismo.mostrar_actividades_sede()