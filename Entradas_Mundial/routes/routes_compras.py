from flask import Blueprint
from Entradas_Mundial.controllers import controller_compras as ctrl
# Asumo que esta es la importación correcta según tu proyecto
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

# Definición del Blueprint
routes_compras = Blueprint('routes_compras', __name__)

# 1. Ruta para seleccionar asientos
@routes_compras.route('/compra/asientos/<int:id_partido>', methods=['GET', 'POST'])
@login_requerido
def seleccionar_asientos(id_partido):
    return ctrl.seleccionar_asientos(id_partido)

# 2. Ruta para completar datos personales
@routes_compras.route('/compra/datos', methods=['GET', 'POST'])
@login_requerido
def datos_comprador():
    return ctrl.datos_comprador()

# 3. Ruta para procesar la compra final
@routes_compras.route('/compra/procesar', methods=['POST'])
@login_requerido
def procesar_compra_final():
    return ctrl.procesar_compra_final()

# 4. Ruta para mostrar la confirmación con el QR
# Asegúrate de que el argumento id_entrada coincida con el controlador
@routes_compras.route('/compra/confirmacion/<int:id_entrada>', methods=['GET'])
@login_requerido
def confirmacion(id_entrada):
    return ctrl.mostrar_confirmacion(id_entrada)