from flask import Flask
from Entradas_Mundial.config import Config
from Entradas_Mundial.models import db

from Entradas_Mundial.models.model_usuarios import UsuarioBase, UsuarioCliente, Administrador 
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada
from Entradas_Mundial.models.model_actividad_turistica import ActividadTuristica, Concierto, ActividadRecreativa

# ELIMINADO/COMENTADO: Esta era la importación que rompía todo
# from Entradas_Mundial.routes.auth import auth_bp

# Tus rutas reales:
from Entradas_Mundial.routes.routes_autenticacion import routes_auth
from Entradas_Mundial.routes.routes_partidos import routes_partidos
from Entradas_Mundial.routes.routes_compras import routes_compras
from Entradas_Mundial.routes.routes_turismo import routes_turismo

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'clave_secreta_mundial_2026'

db.init_app(app)

# Registramos tus blueprints reales
app.register_blueprint(routes_auth)
app.register_blueprint(routes_partidos)
app.register_blueprint(routes_compras)
app.register_blueprint(routes_turismo)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Lógica original para el administrador Priscila
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