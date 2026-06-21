from flask import Blueprint
from Entradas_Mundial.controllers import controller_turismo
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_turismo = Blueprint('routes_turismo', __name__)

@routes_turismo.route('/turismo/recomendaciones')
@login_requerido
def listar_actividades():
    return controller_turismo.mostrar_actividades_sede()