from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from Entradas_Mundial.controllers import controller_autenticacion

routes_auth = Blueprint('routes_auth', __name__)


@routes_auth.route('/')
def index_auth():
    return render_template('auth/index_auth.html')

@routes_auth.route('/login', methods=['GET', 'POST'])
def login():
    return controller_autenticacion.login_usuario()

@routes_auth.route('/registro', methods=['GET', 'POST'])
def registro():
    return controller_autenticacion.registro_usuario()

@routes_auth.route('/logout')
def logout():
    return controller_autenticacion.logout_usuario()

@routes_auth.route('/recuperar-password', methods=['GET', 'POST'])
def recuperar_password():
    return controller_autenticacion.recuperar_password()


@routes_auth.route('/perfil')
@login_required 
def perfil():
    return render_template('auth/perfil.html', usuario=current_user)

@routes_auth.route('/perfil/actualizar_pago', methods=['POST'])
@login_required
def actualizar_pago():
    nuevo_numero = request.form.get('numero_tarjeta')
    if nuevo_numero and len(nuevo_numero.replace(" ", "")) >= 16:
        controller_autenticacion.actualizar_metodo_pago(nuevo_numero)
        flash("Tarjeta actualizada con éxito", "success")
    else:
        flash("Número de tarjeta inválido. Debe tener 16 dígitos.", "danger")
        
    return redirect(url_for('routes_auth.perfil'))