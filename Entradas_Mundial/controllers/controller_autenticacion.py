from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_usuarios import UsuarioCliente, Administrador, UsuarioBase

def index_auth():
    # RUTA ACTUALIZADA: Carpeta auth/
    return render_template('auth/index_auth.html')

def login_usuario():
    if current_user.is_authenticated:
        return redirect(url_for('routes_partidos.lista_partidos'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        es_admin = request.form.get('es_admin') 

        if es_admin:
            dni = request.form.get('dni')
            admin = Administrador.query.filter_by(email=email, _password=password, dni=dni, rol='administrador').first()
            if admin:
                login_user(admin)
                flash('¡Bienvenido Administrador!', 'success')
                return redirect(url_for('routes_partidos.lista_partidos'))
            else:
                flash('Error: Credenciales de administrador incorrectas.', 'danger')
                return redirect(url_for('routes_auth.login'))
        else:
            usuario = UsuarioCliente.query.filter_by(email=email, _password=password, rol='cliente').first()
            if usuario:
                login_user(usuario)
                return redirect(url_for('routes_partidos.lista_partidos'))
            else:
                flash('Error: Usuario o contraseña incorrectos.', 'danger')
                return redirect(url_for('routes_auth.login'))

    # RUTA ACTUALIZADA: Carpeta auth/
    return render_template('auth/login.html')

def registro_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        password = request.form.get('password')
        tarjeta_preferida = request.form.get('tarjeta') 

        if UsuarioBase.query.filter_by(email=email).first():
            flash('El correo ya está registrado.', 'warning')
            return redirect(url_for('routes_auth.registro'))

        nuevo_cliente = UsuarioCliente(
            nombre=nombre, apellido=apellido, email=email,
            password=password, rol='cliente',
            tarjeta_credito_asociada=tarjeta_preferida
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        flash('Registro exitoso. Ya podés iniciar sesión.', 'success')
        return redirect(url_for('routes_auth.login'))

    # RUTA ACTUALIZADA: Carpeta auth/
    return render_template('auth/registro.html')

def logout_usuario():
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('routes_auth.login'))

def recuperar_password():
    if request.method == 'POST':
        email = request.form.get('email')
        nueva_password = request.form.get('nueva_password')
        usuario = UsuarioBase.query.filter_by(email=email).first()
        if usuario:
            usuario.password = nueva_password
            db.session.commit()
            flash('¡Contraseña restablecida!', 'success')
            return redirect(url_for('routes_auth.login'))
        else:
            flash('Correo no registrado.', 'danger')
            
    # RUTA ACTUALIZADA: Carpeta auth/
    return render_template('auth/recuperar_password.html')

login_requerido = login_required