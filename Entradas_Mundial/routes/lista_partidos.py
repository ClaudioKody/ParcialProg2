from flask import Blueprint
from Entradas_Mundial.controllers import controller_partidos
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_partidos = Blueprint('routes_partidos', __name__)

@routes_partidos.route('/partidos')
@login_requerido
def lista_partidos():
    # Muestra el catálogo de partidos o el panel de control si es Admin
    return controller_partidos.listar_partidos_cliente()

@routes_partidos.route('/mis-entradas')
@login_requerido
def mis_entradas():
    # Devuelve el HTML de las entradas compradas por el usuario actual
    return controller_partidos.mostrar_mis_entradas()