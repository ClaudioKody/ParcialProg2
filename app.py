from flask import Flask
from Entradas_Mundial.models import db
from Entradas_Mundial.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializá la base de datos con la app
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)