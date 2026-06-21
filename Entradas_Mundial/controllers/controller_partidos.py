from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_entradas import Entrada

# --- VISTAS DE USUARIO ---

def listar_partidos_cliente():
    query_busqueda = request.args.get('search')
    filtro_ciudad = request.args.get('ciudad')

    partidos_query = Partido.query
    
    if query_busqueda:
        partidos_query = partidos_query.filter(
            (Partido.equipo1.like(f"%{query_busqueda}%")) | 
            (Partido.equipo2.like(f"%{query_busqueda}%"))
        )
        
    if filtro_ciudad:
        partidos_query = partidos_query.filter_by(ciudad=filtro_ciudad)
        
    partidos = partidos_query.all()
    return render_template('partidos/lista_partidos.html', partidos=partidos)

def mostrar_mis_entradas():
    # Filtramos entradas asociadas al usuario actual a través de sus compras
    entradas = Entrada.query.join(Entrada.compra_rel).filter_by(usuario_id=current_user.id).all()
    return render_template('partidos/mis_entradas.html', entradas=entradas)

# --- VISTAS DE ADMINISTRACIÓN ---

@login_required
def crear_partido():
    if not current_user.es_admin:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('routes_partidos.lista_partidos'))
        
    if request.method == 'POST':
        nuevo_partido = Partido(
            equipo1=request.form.get('equipo1'),
            equipo2=request.form.get('equipo2'),
            fecha_hora=request.form.get('fecha_hora'),
            estadio=request.form.get('estadio'),
            ciudad=request.form.get('ciudad'),
            fase=request.form.get('fase'),
            precio_base=float(request.form.get('precio_base')),
            capacidad_estadio=int(request.form.get('capacidad')),
            capacidad_disponible=int(request.form.get('capacidad'))
        )
        db.session.add(nuevo_partido)
        db.session.commit()
        flash('Partido creado exitosamente.', 'success')
        return redirect(url_for('routes_partidos.lista_partidos'))
        
    return render_template('admin/crear_partido.html')

@login_required
def editar_partido(id_partido):
    if not current_user.es_admin:
        return "Acceso denegado", 403
        
    partido = Partido.query.get_or_404(id_partido)
    if request.method == 'POST':
        partido.equipo1 = request.form.get('equipo1')
        partido.equipo2 = request.form.get('equipo2')
        partido.estadio = request.form.get('estadio')
        partido.precio_base = float(request.form.get('precio_base'))
        db.session.commit()
        flash('Partido actualizado.', 'success')
        return redirect(url_for('routes_partidos.lista_partidos'))
        
    return render_template('admin/editar_partido.html', partido=partido)

@login_required
def eliminar_partido(id_partido):
    if not current_user.es_admin:
        return "Acceso denegado", 403
    
    partido = Partido.query.get_or_404(id_partido)
    db.session.delete(partido)
    db.session.commit()
    flash('Partido eliminado correctamente.', 'success')
    return redirect(url_for('routes_partidos.lista_partidos'))