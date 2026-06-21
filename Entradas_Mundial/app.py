from flask import Flask, redirect, url_for
from Entradas_Mundial.config import Config
from Entradas_Mundial.models import db
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

# 1. Inicialización de la aplicación
app = Flask(__name__)

# 2. Carga de configuración (Asegura la SECRET_KEY)
app.config.from_object(Config)

# Fallback de seguridad: si SECRET_KEY no está en config.py, la asignamos aquí
if not app.config.get('SECRET_KEY'):
    app.config['SECRET_KEY'] = 'una_clave_por_defecto_muy_segura_para_desarrollo'

# 3. Inicialización de extensiones
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes_auth.login'

# 4. Cargador de usuarios (Flask-Login)
from Entradas_Mundial.models.model_usuarios import UsuarioBase
@login_manager.user_loader
def load_user(user_id):
    return UsuarioBase.query.get(int(user_id))

# 5. Registro de Blueprints
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

# 6. Contexto de aplicación y ejecución
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        from Entradas_Mundial.models.model_usuarios import Administrador
        
        # Lista unificada de administradores
        lista_admins = [
            {"nombre": "Priscila", "apellido": "Toledano", "email": "admin@mundial.com", "dni": "46664548"},
            {"nombre": "Tomás", "apellido": "Naveda", "email": "admin1@mundial.com", "dni": "46662116"},
            {"nombre": "Claudio", "apellido": "Pérez", "email": "admin2@mundial.com", "dni": "46328090"},
            {"nombre": "Selene", "apellido": "Quintero", "email": "admin3@mundial.com", "dni": "45139959"}
        ]
        
        for datos in lista_admins:
            # Buscamos si el admin ya existe por su email único
            if not Administrador.query.filter_by(email=datos['email']).first():
                admin_nuevo = Administrador(
                    nombre=datos['nombre'],
                    apellido=datos['apellido'],
                    email=datos['email'],
                    password=generate_password_hash("admin123"),
                    rol="administrador",
                    dni=datos['dni']
                )
                db.session.add(admin_nuevo)
                print(f"Administrador {datos['nombre']} registrado correctamente.")
        
        db.session.commit()
            
    app.run(debug=True)