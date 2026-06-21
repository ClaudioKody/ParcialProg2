from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_usuarios import UsuarioCliente, Administrador, UsuarioBase

def login_usuario():
    # Si el usuario ya inició sesión, lo redirigimos directo a los partidos
    if current_user.is_authenticated:
        return redirect(url_for('routes_partidos.lista_partidos'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        es_admin = request.form.get('es_admin') 

        if es_admin:
            dni = request.form.get('dni')
            
            # Usamos _password para consultar directamente a la base de datos respetando el encapsulamiento
            admin = Administrador.query.filter_by(email=email, _password=password, dni=dni, rol='administrador').first()
            
            if admin:
                login_user(admin)
                flash('¡Bienvenido Administrador!', 'success')
                return redirect(url_for('routes_partidos.lista_partidos'))
            else:
                flash('Error: Credenciales de administrador incorrectas o DNI no válido.', 'danger')
                return redirect(url_for('routes_auth.login'))
        else:
            # Usamos _password para consultar directamente a la base de datos
            usuario = UsuarioCliente.query.filter_by(email=email, _password=password, rol='cliente').first()
            
            if usuario:
                login_user(usuario)
                return redirect(url_for('routes_partidos.lista_partidos'))
            else:
                flash('Error: Usuario o contraseña incorrectos.', 'danger')
                return redirect(url_for('routes_auth.login'))

    return render_template('autenticacion/registro.html')

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
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=password, # Pasa por tu validación @password.setter
            rol='cliente',
            tarjeta_credito_asociada=tarjeta_preferida
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        flash('Registro exitoso. Ya podés iniciar sesión.', 'success')
        return redirect(url_for('routes_auth.login'))

    return render_template('autenticacion/registro.html')

def logout_usuario():
    logout_user() # Flask-Login destruye la sesión de forma segura
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('routes_auth.login'))

def recuperar_password():
    if request.method == 'POST':
        email = request.form.get('email')
        nueva_password = request.form.get('nueva_password')
        
        usuario = UsuarioBase.query.filter_by(email=email).first()
        if usuario:
            usuario.password = nueva_password # Pasa por la validación de tu setter
            db.session.commit()
            flash('¡Contraseña restablecida con éxito! Ya podés iniciar sesión.', 'success')
            return redirect(url_for('routes_auth.login'))
        else:
            flash('El correo ingresado no corresponde a ningún usuario registrado.', 'danger')
            
    return render_template('autenticacion/recuperar_password.html')

# TRUCO: Asignamos tu nombre de decorador al decorador oficial de Flask-Login.
# Así no tenés que cambiar las importaciones en tus archivos de rutas.
login_requerido = login_required