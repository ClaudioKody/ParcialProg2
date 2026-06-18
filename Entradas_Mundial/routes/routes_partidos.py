from flask import Blueprint
from Entradas_Mundial.controllers import controller_partidos
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_partidos = Blueprint('partidos', __name__)

@routes_partidos.route('/partidos')
@login_requerido
def inicio_partidos():
    return controller_partidos.listar_partidos_cliente()