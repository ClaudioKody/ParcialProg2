from flask import Flask
from Entradas_Mundial.config import Config
from Entradas_Mundial.models import db

# Importamos todos tus modelos reales de POO para que SQLAlchemy cree las tablas
from Entradas_Mundial.models.model_usuarios import UsuarioBase, UsuarioCliente, Administrador 
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada
from Entradas_Mundial.models.model_actividad_turistica import ActividadTuristica, Concierto, ActividadRecreativa

# Importamos el Blueprint de rutas que creamos para /login y /registro
from Entradas_Mundial.routes.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

# Clave secreta obligatoria en Flask para poder usar sesiones y mensajes flash()
app.secret_key = 'clave_secreta_mundial_2026'

# Inicializá la base de datos con la app
db.init_app(app)

# REGISTRO DEL BLUEPRINT: Con esto Flask reconoce las URLs /login y /registro
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        # Crea todas las tablas en tu MySQL Workbench si no existen todavía 
        db.create_all()
        
        # SECCIÓN DE SEGURIDAD: Buscamos usando el rol correcto 'administrador'
        admin_existe = Administrador.query.filter_by(rol='administrador').first()
        
        if not admin_existe:
            admin_fijo = Administrador(
                nombre="Priscila",
                apellido="Toledano",
                email="admin@mundial.com",
                password="admin123",  # Contraseña inicial de prueba
                rol="administrador",  # <-- CORREGIDO: Coincide con tu polymorphic_identity
                dni="46664548"
            )
            db.session.add(admin_fijo)
            db.session.commit()
            print("¡Administrador oficial registrado con éxito en MySQL!")
        else:
            print("El administrador oficial ya está registrado en la base de datos.")
            
    print("¡Aplicación Flask corriendo en modo debug!")
    app.run(debug=True)