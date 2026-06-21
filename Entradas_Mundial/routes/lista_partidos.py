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
def mostrar_mis_entradas():
    return controller_partidos.mostrar_mis_entradas()

@routes_partidos.route('/admin/crear-partido', methods=['GET', 'POST'])
@login_requerido
def crear_partido():
    return controller_partidos.crear_partido()

@routes_partidos.route('/admin/editar-partido/<int:id_partido>', methods=['GET', 'POST'])
@login_requerido
def editar_partido(id_partido):
    return controller_partidos.editar_partido(id_partido)

@routes_partidos.route('/admin/eliminar-partido/<int:id_partido>')
@login_requerido
def eliminar_partido(id_partido):
    return controller_partidos.eliminar_partido(id_partido)