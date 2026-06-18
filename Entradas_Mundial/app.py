from flask import Flask
from Entradas_Mundial.config import Config

# 1. Importamos la db directamente desde la carpeta 'models'
from Entradas_Mundial.models import db

# 2. IMPORTACIÓN DE MODELOS: Con los nombres exactos de tus archivos
from Entradas_Mundial.models.model_usuarios import UsuarioBase, UsuarioCliente, Administrador 
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada
from Entradas_Mundial.models.model_actividad_turistica import ActividadTuristica, Concierto, ActividadRecreativa

app = Flask(__name__)
app.config.from_object(Config)

# Inicializá la base de datos con la app
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        # Crea todas las tablas en tu MySQL si no existen todavía 
        db.create_all()
        
        # SECCIÓN DE SEGURIDAD: Registramos al Administrador Fijo
        admin_existe = Administrador.query.filter_by(rol='admin').first()
        
        if not admin_existe:
            admin_fijo = Administrador(
                nombre="Priscila",
                apellido="Toledano",
                email="admin@mundial.com",
                password="admin123",  # Usamos 'password' tal cual como está en tu model_usuarios
                rol="admin",
                dni="46664548"
            )
            db.session.add(admin_fijo)
            db.session.commit()
            print("¡Administrador oficial registrado con éxito en MySQL!")
        else:
            print("El administrador oficial ya está registrado en la base de datos.")
            
    app.run(debug=True)