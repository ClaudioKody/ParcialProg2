from flask import Blueprint
from Entradas_Mundial.controllers import controller_compras
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_compras = Blueprint('routes_compras', __name__)

@routes_compras.route('/compra/asientos/<int:id_partido>', methods=['GET', 'POST'])
@login_requerido
def seleccionar_asientos(id_partido):
    # Paso 2: Mapa del estadio y cantidad
    return controller_compras.procesar_seleccion_asientos(id_partido)

@routes_compras.route('/compra/datos', methods=['GET', 'POST'])
@login_requerido
def datos_comprador():
    # Paso 3: Formulario de DNI, Nombre, Apellido
    return controller_compras.procesar_datos_comprador()

@routes_compras.route('/compra/pago', methods=['GET', 'POST'])
@login_requerido
def pago():
    # Paso 4: Tarjeta de crédito y cuenta regresiva
    return controller_compras.procesar_pago_tarjeta()

@routes_compras.route('/compra/confirmacion')
@login_requerido
def confirmacion():
    # Paso 5: Generación de QR y ticket final
    return controller_compras.mostrar_confirmacion()



