from flask import Blueprint
from Entradas_Mundial.controllers import controller_compras
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_compras = Blueprint('compras', __name__)

@routes_compras.route('/compra/<int:id_partido>', methods=['GET', 'POST'])
@login_requerido
def proceso_compra(id_partido):
    return controller_compras.procesar_compra_pasos(id_partido)

@routes_compras.route('/compra/confirmacion')
@login_requerido
def confirmacion_ticket():
    return controller_compras.mostrar_confirmacion()