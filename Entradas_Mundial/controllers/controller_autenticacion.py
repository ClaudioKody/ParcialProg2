from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_usuarios import UsuarioCliente, Administrador, UsuarioBase

def login_usuario():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        es_admin = request.form.get('es_admin') == 'on'

        usuario = UsuarioBase.query.filter_by(email=email).first()

        
        if usuario and check_password_hash(usuario.password, password):
            
            
            if es_admin:
                if usuario.rol == 'administrador':
                    dni_ingresado = request.form.get('dni')
                    admin = Administrador.query.filter_by(id=usuario.id, dni=dni_ingresado).first()
                    
                    if admin:
                        login_user(usuario)
                        return redirect(url_for('routes_partidos.lista_partidos'))
                    else:
                        flash('DNI de administrador incorrecto.', 'danger')
                        return redirect(url_for('routes_auth.login'))
                else:
                    flash('Este usuario no tiene rol de administrador.', 'danger')
                    return redirect(url_for('routes_auth.login'))

            else:
                if usuario.rol == 'cliente':
                    login_user(usuario)
                    return redirect(url_for('routes_partidos.lista_partidos'))
                else:
                    flash('Rol de usuario inválido para acceso cliente.', 'danger')
                    return redirect(url_for('routes_auth.login'))

        flash('Credenciales incorrectas.', 'danger')
        return redirect(url_for('routes_auth.login')) 

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
            nombre=nombre, 
            apellido=apellido, 
            email=email,
            password=generate_password_hash(password),
            rol='cliente',
            tarjeta_credito_asociada=tarjeta_preferida
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        flash('Registro exitoso.', 'success')
        return redirect(url_for('routes_auth.login'))

    return render_template('auth/registro.html')

def logout_usuario():
    logout_user()
    return redirect(url_for('routes_auth.login'))

def recuperar_password():
    if request.method == 'POST':
        email = request.form.get('email')
        nueva_password = request.form.get('nueva_password')
        usuario = UsuarioBase.query.filter_by(email=email).first()
        if usuario:
            usuario.password = generate_password_hash(nueva_password)
            flash('¡Contraseña restablecida!', 'success')
            return redirect(url_for('routes_auth.login'))
        flash('Correo no registrado.', 'danger')
            
    return render_template('auth/recuperar_password.html')

login_requerido = login_required

def actualizar_metodo_pago(nuevo_numero_completo):
    numero_limpio = nuevo_numero_completo.replace(" ", "")
    ultimos_cuatro = numero_limpio[-4:]
    if current_user.rol == 'cliente':
        cliente = UsuarioCliente.query.get(current_user.id)
        if cliente:
            cliente.tarjeta_credito_asociada = f"**** **** **** {ultimos_cuatro}"
            db.session.commit()
            return True
            
    return False 