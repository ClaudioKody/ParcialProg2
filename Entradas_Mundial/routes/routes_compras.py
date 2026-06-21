from flask import Blueprint , render_template
from Entradas_Mundial.controllers import controller_compras
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido
from Entradas_Mundial.models.model_entradas import Entrada

routes_compras = Blueprint('routes_compras', __name__)

@routes_compras.route('/compra/asientos/<int:id_partido>', methods=['GET', 'POST'])
@login_requerido
def seleccionar_asientos(id_partido):
    # Llama a la función integrada que procesa el POST y renderiza
    return controller_compras.procesar_compra_pasos(id_partido)

@routes_compras.route('/compra/datos', methods=['GET', 'POST'])
@login_requerido
def datos_comprador():
    return controller_compras.procesar_datos_comprador()

@routes_compras.route('/compra/pago', methods=['GET', 'POST'])
@login_requerido
def pago():
    return controller_compras.procesar_pago_tarjeta()

@routes_compras.route('/compra/confirmacion')
@login_requerido
def confirmacion_de_compra():
    return controller_compras.mostrar_confirmacion()

@routes_compras.route('/compra/confirmacion/<int:id_entrada>')
@login_requerido
def confirmacion(id_entrada):
    # Aquí buscas la entrada por su ID y renderizas el template
    entrada = Entrada.query.get_or_404(id_entrada)
    return render_template('compra/confirmacion.html', entrada=entrada)