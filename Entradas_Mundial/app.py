from flask import Flask, app, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def mostrar_login():
    return render_template('iniciosesion.html')

@app.route('/login', methods=['POST'])
def procesar_login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and password == 'password':
        return render_template('bienvenido', username=username)
    else:
        return render_template('iniciosesion.html', error='Credenciales incorrectas')
    

if __name__ == '__main__':
    app.run(debug=True)