from flask import render_template, request, redirect, url_for, flash, session
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_partido import Partido

def listar_partidos_cliente():
    query_busqueda = request.args.get('search')
    filtro_ciudad = request.args.get('ciudad')
    
    # Base de la consulta
    partidos_query = Partido.query
    
    # Lógica de la barra de búsqueda (Busca por país local o visitante)
    if query_busqueda:
        partidos_query = partidos_query.filter(
            (Partido.pais_local.like(f"%{query_busqueda}%")) | 
            (Partido.pais_visitante.like(f"%{query_busqueda}%"))
        )
        
    # Filtros del panel izquierdo (image_18cd06.png)
    if filtro_ciudad:
        partidos_query = partidos_query.filter_by(ciudad=filtro_ciudad)
        
    partidos = partidos_query.all()
    return render_template('partidos.html', partidos=partidos)

# --- OPERACIONES CRUD (Para el Administrador) ---

def crear_partido():
    if session.get('user_rol') != 'admin': return "Acceso denegado", 403
    if request.method == 'POST':
        nuevo_partido = Partido(
            pais_local=request.form.get('pais_local'),
            pais_visitante=request.form.get('pais_visitante'),
            fecha_hora=request.form.get('fecha_hora'),
            estadio=request.form.get('estadio'),
            ciudad=request.form.get('ciudad'),
            precio_base=float(request.form.get('precio_base')),
            capacidad_disponible=int(request.form.get('capacidad'))
        )
        db.session.add(nuevo_partido)
        db.session.commit()
        flash('Partido creado exitosamente.', 'success')
        return redirect(url_for('panel_administrador'))
    return render_template('admin/crear_partido.html')

def editar_partido(id_partido):
    if session.get('user_rol') != 'admin': return "Acceso denegado", 403
    partido = Partido.query.get_or_404(id_partido)
    if request.method == 'POST':
        partido.pais_local = request.form.get('pais_local')
        partido.pais_visitante = request.form.get('pais_visitante')
        partido.estadio = request.form.get('estadio')
        partido.precio_base = float(request.form.get('precio_base'))
        db.session.commit()
        flash('Partido actualizado.', 'success')
        return redirect(url_for('panel_administrador'))
    return render_template('admin/editar_partido.html', partido=partido)

def eliminar_partido(id_partido):
    if session.get('user_rol') != 'admin': return "Acceso denegado", 403
    partido = Partido.query.get_or_404(id_partido)
    db.session.delete(partido)
    db.session.commit()
    flash('Partido eliminado correctamente.', 'success')
    return redirect(url_for('panel_administrador'))