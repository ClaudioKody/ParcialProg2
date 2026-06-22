from flask import Blueprint , redirect, url_for
from Entradas_Mundial.controllers import controller_compras as ctrl 
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido
from Entradas_Mundial.models.model_entradas import Entrada

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
    # 1. Tu lógica actual para guardar la entrada en la base de datos...
    # Ejemplo (ajústalo a cómo guardas tú):
    nueva_entrada = Entrada(...) 
    db.session.add(nueva_entrada)
    db.session.commit() 

    return redirect(url_for('routes_compras.confirmacion', id_entrada=nueva_entrada.id))

# Cambia esta ruta:
@routes_compras.route('/compra/confirmacion/<int:id_entrada>', methods=['GET'])
@login_requerido
def confirmacion(id_entrada): # <--- Ahora recibe el argumento
    return ctrl.mostrar_confirmacion(id_entrada)