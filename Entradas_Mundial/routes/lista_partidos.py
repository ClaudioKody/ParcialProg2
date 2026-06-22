from flask import Blueprint
from flask_login import current_user
from Entradas_Mundial.controllers import controller_partidos
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido
from Entradas_Mundial.models.model_usuarios import UsuarioBase as Usuario
from flask import Blueprint, render_template, flash, redirect, url_for 


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

@routes_partidos.route('/admin/usuarios')
@login_requerido
def listar_usuarios():
    
    if not current_user.es_admin:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('routes_partidos.lista_partidos'))
        
    usuarios = Usuario.query.all()
    return render_template('admin/lista_usuarios.html', usuarios=usuarios)

@routes_partidos.route('/admin/banear-usuario/<int:id_usuario>')
@login_requerido
def banear_usuario(id_usuario):
    return redirect(url_for('routes_partidos.listar_usuarios'))