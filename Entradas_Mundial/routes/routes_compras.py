from flask import Blueprint
from Entradas_Mundial.controllers import controller_compras as ctrl
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_compras = Blueprint('routes_compras', __name__)

@routes_compras.route('/compra/asientos/<int:id_partido>', methods=['GET', 'POST'])
@login_requerido
def seleccionar_asientos(id_partido):
    return ctrl.seleccionar_asientos(id_partido)

@routes_compras.route('/compra/datos', methods=['GET', 'POST'])
@login_requerido
def datos_comprador():
    return ctrl.datos_comprador()

@routes_compras.route('/compra/procesar', methods=['POST'])
@login_requerido
def procesar_compra_final():
    return ctrl.procesar_compra_final()


@routes_compras.route('/compra/confirmacion/<int:id_entrada>', methods=['GET'])
@login_requerido
def confirmacion(id_entrada):
    return ctrl.mostrar_confirmacion(id_entrada)