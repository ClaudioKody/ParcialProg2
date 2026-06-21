from flask import Flask, redirect, url_for
from Entradas_Mundial.config import Config
from Entradas_Mundial.models import db
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ==================== CONFIGURACIÓN DE FLASK-LOGIN ====================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes_auth.login'  # Apunta a la ruta de login

# Importación centralizada para cargar el user_loader
from Entradas_Mundial.models.model_usuarios import UsuarioBase

@login_manager.user_loader
def load_user(user_id):
    return UsuarioBase.query.get(int(user_id))

# ==================== IMPORTACIÓN DE RUTAS (BLUEPRINTS) ====================
from Entradas_Mundial.routes.routes_auth import routes_auth
from Entradas_Mundial.routes.lista_partidos import routes_partidos
from Entradas_Mundial.routes.routes_compras import routes_compras
from Entradas_Mundial.routes.ver_turismo import routes_turismo
from Entradas_Mundial.routes.routes_ayuda import routes_ayuda

app.register_blueprint(routes_auth, url_prefix='/auth')
app.register_blueprint(routes_partidos, url_prefix='/partidos')
app.register_blueprint(routes_compras, url_prefix='/compras')
app.register_blueprint(routes_turismo, url_prefix='/turismo')
app.register_blueprint(routes_ayuda, url_prefix='/ayuda')

@app.route('/')
def inicio():
    return redirect(url_for('routes_auth.index_auth'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Creación del Administrador con contraseña hasheada
        from Entradas_Mundial.models.model_usuarios import Administrador
        admin_existe = Administrador.query.filter_by(rol='administrador').first()
        
        if not admin_existe:
            admin_fijo = Administrador(
                nombre="Priscila",
                apellido="Toledano",
                email="admin@mundial.com",
                password=generate_password_hash("admin123"), # IMPORTANTE: Hashear aquí
                rol="administrador",
                dni="46664548"
            )
            db.session.add(admin_fijo)
            db.session.commit()
            print("Administrador registrado correctamente.")
            
    app.run(debug=True)