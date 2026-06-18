from flask import Flask
from Entradas_Mundial.config import Config
from Entradas_Mundial.models import db

<<<<<<< HEAD
=======

app = Flask(__name__)
app.config.from_object(Config)


app.secret_key = 'clave_secreta_mundial_2026'


db.init_app(app)


>>>>>>> 38e0a8096b7bd40d1930d654c1e19c2ac5584479
from Entradas_Mundial.models.model_usuarios import UsuarioBase, UsuarioCliente, Administrador 
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_compra import Compra
from Entradas_Mundial.models.model_entradas import Entrada
from Entradas_Mundial.models.model_actividad_turistica import ActividadTuristica, Concierto, ActividadRecreativa

<<<<<<< HEAD
from Entradas_Mundial.routes.auth import auth_bp
=======
>>>>>>> 38e0a8096b7bd40d1930d654c1e19c2ac5584479

from Entradas_Mundial.routes.routes_autenticacion import routes_auth
from Entradas_Mundial.routes.routes_partidos import routes_partidos
from Entradas_Mundial.routes.routes_compras import routes_compras
from Entradas_Mundial.routes.routes_turismo import routes_turismo

<<<<<<< HEAD
app.secret_key = 'clave_secreta_mundial_2026'

db.init_app(app)

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
=======

app.register_blueprint(routes_auth)
app.register_blueprint(routes_partidos)
app.register_blueprint(routes_compras)
app.register_blueprint(routes_turismo)

if __name__ == '__main__':
    with app.app_context():
       
        db.create_all()
        
        
>>>>>>> 38e0a8096b7bd40d1930d654c1e19c2ac5584479
        admin_existe = Administrador.query.filter_by(rol='administrador').first()
        
        if not admin_existe:
            admin_fijo = Administrador(
                nombre="Priscila",
                apellido="Toledano",
                email="admin@mundial.com",
<<<<<<< HEAD
                password="admin123", 
=======
                password="admin123",  
>>>>>>> 38e0a8096b7bd40d1930d654c1e19c2ac5584479
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