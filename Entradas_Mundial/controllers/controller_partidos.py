from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from datetime import datetime
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_partido import Partido
from Entradas_Mundial.models.model_entradas import Entrada
from Entradas_Mundial.models.model_compra import Compra

# --- VISTAS DE USUARIO ---

@login_required
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
    
    # 2. Pasamos 'ahora' al template para hacer la comparación en el HTML
    return render_template(
        'partidos/lista_partidos.html', 
        partidos=partidos, 
        ahora=datetime.now()
    )
@login_required
def mostrar_mis_entradas():
    compras_usuario = Compra.query.filter_by(usuario_id=current_user.id).all()
    ids_compras = [compra.id for compra in compras_usuario]
    
    lista_entradas = Entrada.query.filter(Entrada.compra_id.in_(ids_compras)).all()
    
    hoy = datetime.now()
    proximos = []
    historial = []
    
    for entrada in lista_entradas:
        if entrada.partido_rel.fecha_hora > hoy:
            proximos.append(entrada)
        else:
            historial.append(entrada)
            
    return render_template('partidos/mis_entradas.html', 
                           proximos=proximos, 
                           historial=historial)
@login_required
def crear_partido():
    if not current_user.es_admin:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('routes_partidos.lista_partidos'))
        
    if request.method == 'POST':
        # ... (tu lógica de guardado sigue igual) ...
        return redirect(url_for('routes_partidos.lista_partidos'))
        
    # CAMBIO AQUÍ: de 'admin/crear_partido.html' a 'partidos/crear_partido.html'
    return render_template('admin/crear_partido.html')

@login_required
def editar_partido(id_partido):
    if not current_user.es_admin:
        return "Acceso denegado", 403
        
    partido = Partido.query.get_or_404(id_partido)
    if request.method == 'POST':
        # ... (tu lógica de guardado sigue igual) ...
        return redirect(url_for('routes_partidos.lista_partidos'))
        
    # CAMBIO AQUÍ: de 'admin/editar_partido.html' a 'partidos/editar_partido.html'
    return render_template('partidos/editar_partido.html', partido=partido)

@login_required
def eliminar_partido(id_partido):
    if not current_user.es_admin:
        return "Acceso denegado", 403
    
    partido = Partido.query.get_or_404(id_partido)
    db.session.delete(partido)
    db.session.commit()
    flash('Partido eliminado correctamente.', 'success')
    return redirect(url_for('routes_partidos.lista_partidos'))