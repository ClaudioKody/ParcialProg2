from flask import Blueprint
from Entradas_Mundial.controllers import controller_partidos
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_partidos = Blueprint('routes_partidos', __name__)

@routes_partidos.route('/partidos')
@login_requerido
def lista_partidos():
    
    return controller_partidos.listar_partidos_cliente()

@routes_partidos.route('/mis-entradas')
@login_requerido
def mis_entradas():
    
    return controller_partidos.mostrar_mis_entradas()