from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import db  # Importa la base de datos vinculada
# Importamos la clase específica que utiliza el proyecto para los compradores
from ..models.model_usuarios import UsuarioCliente 
from werkzeug.security import generate_password_hash, check_password_hash

# Creamos el Blueprint para Autenticación
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Buscamos al usuario en la base de datos 'mundial'
        usuario = UsuarioCliente.query.filter_by(email=email).first()
        
        # Verificamos si existe el usuario
        if usuario:
            # Soporte doble: verifica por hash encriptado o por texto plano directo
            if check_password_hash(usuario.password, password) or usuario.password == password:
                # ¡Login exitoso! Redirige al panel principal del mundial
                return redirect(url_for('auth.dashboard'))
        
        # Si los datos están mal
        flash('Correo electrónico o contraseña incorrectos', 'danger')
        
    return render_template('iniciosesion.html')

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        
        # Validaciones de contraseñas
        if password != password_confirm:
            flash('Las contraseñas no coinciden', 'danger')
            return render_template('registro.html')
            
        # Verificar si el correo ya está registrado en MySQL
        user_exists = UsuarioCliente.query.filter_by(email=email).first()
        if user_exists:
            flash('El correo electrónico ya está registrado', 'danger')
            return render_template('registro.html')
            
        # Encriptamos la contraseña por seguridad antes de guardarla
        hashed_password = generate_password_hash(password, method='scrypt')
        
        # Creamos el nuevo objeto utilizando tu clase UsuarioCliente (POO)
        nuevo_usuario = UsuarioCliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=hashed_password,
            rol='Usuario' # Rol estándar para los clientes de entradas
        )
        
        # Guardamos el registro en Workbench
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('¡Cuenta creada con éxito! Ya podés iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('Hubo un error al crear la cuenta. Intentalo de nuevo.', 'danger')
            
    return render_template('registro.html')

@auth_bp.route('/dashboard')
def dashboard():
    # Esta será la página protegida para los usuarios autenticados
    return "<h1>Bienvenido al Sistema de Entradas del Mundial 2026</h1><p>Próximamente: Lista de partidos para comprar.</p>"