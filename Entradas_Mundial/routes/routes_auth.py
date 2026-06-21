from flask import Blueprint, render_template
from Entradas_Mundial.controllers import controller_autenticacion

routes_auth = Blueprint('routes_auth', __name__)

@routes_auth.route('/')
def index_auth():
    ## Cambio de ruta: carpeta auth/
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