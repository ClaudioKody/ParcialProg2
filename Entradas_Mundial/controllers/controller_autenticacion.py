from flask import render_template, request, redirect, url_for, session, flash
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_usuarios import UsuarioCliente, Administrador, UsuarioBase

def login_usuario():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        es_admin = request.form.get('es_admin') 

        if es_admin:
            dni = request.form.get('dni')
            
            admin = Administrador.query.filter_by(email=email, password=password, dni=dni, rol='admin').first()
            if admin:
                session['user_id'] = admin.id
                session['user_nombre'] = admin.nombre
                session['user_rol'] = 'admin'
                flash('¡Bienvenido Administrador!', 'success')
                return redirect(url_for('panel_administrador'))
            else:
                flash('Error: Credenciales de administrador incorrectas o DNI no válido.', 'danger')
                return redirect(url_for('login'))
        else:
            # Login para usuario común
            usuario = UsuarioCliente.query.filter_by(email=email, password=password, rol='cliente').first()
            if usuario:
                session['user_id'] = usuario.id
                session['user_nombre'] = usuario.nombre
                session['user_rol'] = 'cliente'
                return redirect(url_for('inicio_partidos'))
            else:
                flash('Error: Usuario o contraseña incorrectos.', 'danger')
                return redirect(url_for('login'))

    return render_template('login.html')

def registro_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        password = request.form.get('password')
        tarjeta_preferida = request.form.get('tarjeta') 

       
        if UsuarioBase.query.filter_by(email=email).first():
            flash('El correo ya está registrado.', 'warning')
            return redirect(url_for('registro'))

        nuevo_cliente = UsuarioCliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=password,
            rol='cliente',
            tarjeta_credito_asociada=tarjeta_preferida
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        flash('Registro exitoso. Ya podés iniciar sesión.', 'success')
        return redirect(url_for('login'))

    return render_template('registro.html')

def logout_usuario():
    session.clear()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))


def recuperar_password():
    if request.method == 'POST':
        email = request.form.get('email')
        nueva_password = request.form.get('nueva_password')
        
        usuario = UsuarioBase.query.filter_by(email=email).first()
        if usuario:
            usuario.password = nueva_password
            db.session.commit()
            flash('¡Contraseña restablecida con éxito! Ya podés iniciar sesión.', 'success')
            return redirect(url_for('login'))
        else:
            flash('El correo ingresado no corresponde a ningún usuario registrado.', 'danger')
            
    return render_template('recuperar_password.html')


def login_requerido(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, iniciá sesión para acceder a esta sección.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function