from flask import Blueprint, render_template
from Entradas_Mundial.controllers.controller_autenticacion import login_requerido

routes_ayuda = Blueprint('routes_ayuda', __name__)

@routes_ayuda.route('/ayuda')
@login_requerido
def ayuda():
    
    return render_template('ayuda.html')