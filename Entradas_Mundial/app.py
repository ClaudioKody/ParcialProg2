from flask import Flask, redirect, url_for
from Entradas_Mundial.config import Config
from Entradas_Mundial.models import db

app = Flask(__name__)
app.config.from_object(Config)

# Clave secreta para manejo de sesiones y cookies seguras
app.secret_key = 'clave_secreta_mundial_2026'

# Inicialización de SQLAlchemy con la App
db.init_app(app)

# ==================== IMPORTACIÓN DE MODELOS (POO) ====================
from Entradas_Mundial.models.model_usuarios import UsuarioBase, UsuarioCliente, Administrador 
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada
from Entradas_Mundial.models.model_actividad_turistica import ActividadTuristica, Concierto, ActividadRecreativa

# ==================== IMPORTACIÓN DE CONTROLADORES DE RUTA ====================
from Entradas_Mundial.routes.routes_auth import routes_auth
from Entradas_Mundial.routes.lista_partidos import routes_partidos
from Entradas_Mundial.routes.routes_compras import routes_compras
from Entradas_Mundial.routes.ver_turismo import routes_turismo
from Entradas_Mundial.routes.routes_ayuda import routes_ayuda

# ==================== REGISTRO DE BLUEPRINTS EN FLASK ====================
app.register_blueprint(routes_auth)
app.register_blueprint(routes_partidos)
app.register_blueprint(routes_compras)
app.register_blueprint(routes_turismo)
app.register_blueprint(routes_ayuda)

# RUTA RAÍZ: Redirige automáticamente a la pantalla de bienvenida / login
@app.route('/')
def inicio():
    return redirect(url_for('routes_auth.index_auth'))

# ==================== ARRANQUE DE LA APLICACIÓN ====================
if __name__ == '__main__':
    with app.app_context():
        # Crea las tablas en MySQL si no existen en base a tus clases de modelos
        db.create_all()
        
        # Validación y carga del Administrador por Defecto
        admin_existe = Administrador.query.filter_by(rol='administrador').first()
        
        if not admin_existe:
            admin_fijo = Administrador(
                nombre="Priscila",
                apellido="Toledano",
                email="admin@mundial.com",
                password="admin123",  
                rol="administrador",  
                dni="46664548"
            )
            db.session.add(admin_fijo)
            db.session.commit()
            print("¡Administrador oficial registrado con éxito en MySQL!")
        else:
            print("El administrador oficial ya está registrado en la base de datos.")
            
    print("¡Aplicación Flask corriendo en modo debug!")
    app.run(debug=True)