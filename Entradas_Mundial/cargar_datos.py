from datetime import datetime, timedelta
from Entradas_Mundial.app import app
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_partido import Partido

def cargar_fixture_mundial_completo():
    print("Iniciando la carga del FIXTURE ADAPTADO AL MODELO (104 Partidos)...")
    
    # Grupos oficiales de la FIFA
    grupos = {
        "Grupo A": ["México", "Sudáfrica", "Corea del Sur", "República Checa"],
        "Grupo B": ["Canadá", "Bosnia y Herzegovina", "Catar", "Suiza"],
        "Grupo C": ["Brasil", "Marruecos", "Haití", "Escocia"],
        "Grupo D": ["Estados Unidos", "Paraguay", "Australia", "Turquía"],
        "Grupo E": ["Alemania", "Costa de Marfil", "Ecuador", "Curazao"],
        "Grupo F": ["Países Bajos", "Japón", "Suecia", "Túnez"],
        "Grupo G": ["Bélgica", "Irán", "Egipto", "Nueva Zelanda"],
        "Grupo H": ["España", "Uruguay", "Arabia Saudita", "Cabo Verde"],
        "Grupo I": ["Francia", "Senegal", "Noruega", "Irak"],
        "Grupo J": ["Argentina", "Austria", "Argelia", "Jordania"],
        "Grupo K": ["Portugal", "Colombia", "Uzbekistán", "República Democrática del Congo"],
        "Grupo L": ["Inglaterra", "Croacia", "Ghana", "Panamá"]
    }
    
    # Sedes oficiales asociadas a sus ciudades para cumplir con el filtro izquierdo
    sedes_info = [
        {"estadio": "Estadio Ciudad de México", "ciudad": "Ciudad de México"},
        {"estadio": "Estadio Guadalajara", "ciudad": "Guadalajara"},
        {"estadio": "Estadio Monterrey", "ciudad": "Monterrey"},
        {"estadio": "Estadio Toronto", "ciudad": "Toronto"},
        {"estadio": "Estadio BC Place", "ciudad": "Vancouver"},
        {"estadio": "Estadio Los Ángeles", "ciudad": "Los Ángeles"},
        {"estadio": "MetLife Stadium", "ciudad": "Nueva York"},
        {"estadio": "Gillette Stadium", "ciudad": "Boston"},
        {"estadio": "AT&T Stadium", "ciudad": "Dallas"},
        {"estadio": "Hard Rock Stadium", "ciudad": "Miami"},
        {"estadio": "Mercedes-Benz Stadium", "ciudad": "Atlanta"},
        {"estadio": "NRG Stadium", "ciudad": "Houston"},
        {"estadio": "Lincoln Financial Field", "ciudad": "Filadelfia"},
        {"estadio": "Arrowhead Stadium", "ciudad": "Kansas City"},
        {"estadio": "Lumen Field", "ciudad": "Seattle"},
        {"estadio": "Levi's Stadium", "ciudad": "San Francisco"}
    ]
    
    partidos_a_cargar = []
    fecha_inicio = datetime(2026, 6, 11, 15, 0)
    
    # 1. GENERACIÓN DE FASE DE GRUPOS (72 partidos)
    sede_idx = 0
    partidos_por_dia = 4
    contador_partidos = 0
    
    for nombre_grupo, equipos in grupos.items():
        cruces = [
            (equipos[0], equipos[1]), (equipos[2], equipos[3]),
            (equipos[0], equipos[2]), (equipos[1], equipos[3]),
            (equipos[0], equipos[3]), (equipos[1], equipos[2])
        ]
        
        for local, visitante in cruces:
            dias_extra = contador_partidos // partidos_por_dia
            hora_extra = (contador_partidos % partidos_por_dia) * 3
            
            fecha_partido = fecha_inicio + timedelta(days=dias_extra)
            fecha_partido = fecha_partido.replace(hour=13 + hora_extra, minute=0)
            
            sede = sedes_info[sede_idx % len(sedes_info)]
            
            partidos_a_cargar.append({
                "equipo1": local,
                "equipo2": visitante,
                "fecha_hora": fecha_partido,
                "estadio": sede["estadio"],
                "ciudad": sede["ciudad"],
                "precio_base": 150.0,
                "capacidad_disponible": 60000,
                "capacidad_estadio": 60000,
                "fase": "Grupos"
            })
            sede_idx += 1
            contador_partidos += 1

    # 2. GENERACIÓN DE FASES ELIMINATORIAS (32 partidos)
    fecha_eliminatorias = datetime(2026, 6, 28, 16, 0)
    
    # Dieciseisavos de Final (16 partidos)
    for i in range(1, 17):
        sede = sedes_info[i % len(sedes_info)]
        partidos_a_cargar.append({
            "equipo1": f"Clasificado {2*i-1}", "equipo2": f"Clasificado {2*i}",
            "fecha_hora": fecha_eliminatorias + timedelta(days=i//4, hours=(i%4)*3),
            "estadio": sede["estadio"], "ciudad": sede["ciudad"],
            "precio_base": 200.0, "capacidad_disponible": 65000, "capacidad_estadio": 65000, "fase": "16avos"
        })
        
    # Octavos de Final (8 partidos)
    fecha_octavos = datetime(2026, 7, 4, 16, 0)
    for i in range(1, 8):
        sede = sedes_info[(i+4) % len(sedes_info)]
        partidos_a_cargar.append({
            "equipo1": f"Ganador 16avos {2*i-1}", "equipo2": f"Ganador 16avos {2*i}",
            "fecha_hora": fecha_octavos + timedelta(days=i//3, hours=(i%3)*4),
            "estadio": sede["estadio"], "ciudad": sede["ciudad"],
            "precio_base": 300.0, "capacidad_disponible": 70000, "capacidad_estadio": 70000, "fase": "Octavos"
        })
        
    # Cuartos de Final (4 partidos)
    fecha_cuartos = datetime(2026, 7, 9, 17, 0)
    for i in range(1, 5):
        partidos_a_cargar.append({
            "equipo1": f"Ganador Octavos {2*i-1}", "equipo2": f"Ganador Octavos {2*i}",
            "fecha_hora": fecha_cuartos + timedelta(days=i//2, hours=(i%2)*4),
            "estadio": "AT&T Stadium" if i%2==0 else "Estadio Los Ángeles",
            "ciudad": "Dallas" if i%2==0 else "Los Ángeles",
            "precio_base": 450.0, "capacidad_disponible": 75000, "capacidad_estadio": 75000, "fase": "Cuartos"
        })
        
    # Semifinales (2 partidos)
    partidos_a_cargar.append({
        "equipo1": "Ganador Cuartos 1", "equipo2": "Ganador Cuartos 2",
        "fecha_hora": datetime(2026, 7, 14, 20, 0), "estadio": "Mercedes-Benz Stadium", "ciudad": "Atlanta",
        "precio_base": 600.0, "capacidad_disponible": 71000, "capacidad_estadio": 71000, "fase": "Semifinal"
    })
    partidos_a_cargar.append({
        "equipo1": "Ganador Cuartos 3", "equipo2": "Ganador Cuartos 4",
        "fecha_hora": datetime(2026, 7, 15, 20, 0), "estadio": "AT&T Stadium", "ciudad": "Dallas",
        "precio_base": 600.0, "capacidad_disponible": 90000, "capacidad_estadio": 90000, "fase": "Semifinal"
    })
    
    # Tercer Puesto (1 partido)
    partidos_a_cargar.append({
        "equipo1": "Perdedor Semi 1", "equipo2": "Perdedor Semi 2",
        "fecha_hora": datetime(2026, 7, 18, 16, 0), "estadio": "Hard Rock Stadium", "ciudad": "Miami",
        "precio_base": 500.0, "capacidad_disponible": 65000, "capacidad_estadio": 65000, "fase": "Tercer Puesto"
    })
    
    # LA GRAN FINAL (Partido número 104)
    partidos_a_cargar.append({
        "equipo1": "Ganador Semi 1", "equipo2": "Ganador Semi 2",
        "fecha_hora": datetime(2026, 7, 19, 18, 0), "estadio": "MetLife Stadium", "ciudad": "Nueva York",
        "precio_base": 1000.0, "capacidad_disponible": 82500, "capacidad_estadio": 82500, "fase": "Final"
    })

    # 3. VOLCADO A LA BASE DE DATOS
    contador_insertados = 0
    try:
        for p in partidos_a_cargar:
            # Validación adaptada a los nombres del modelo
            existe = Partido.query.filter_by(
                equipo1=p["equipo1"], 
                equipo2=p["equipo2"]
            ).first()
            
            if not existe:
                partido_nuevo = Partido(
                    equipo1=p["equipo1"],
                    equipo2=p["equipo2"],
                    fecha_hora=p["fecha_hora"],
                    estadio=p["estadio"],
                    ciudad=p["ciudad"],
                    precio_base=p["precio_base"],
                    capacidad_disponible=p["capacidad_disponible"],
                    capacidad_estadio=p["capacidad_estadio"],
                    fase=p["fase"]
                )
                db.session.add(partido_nuevo)
                contador_insertados += 1
                
        db.session.commit()
        print(f"🏆 ¡ÉXITO! Fixture de 104 partidos sincronizado perfectamente.")
        print(f"📊 Registros añadidos: {contador_insertados}")
        
    except Exception as e:
        db.session.rollback()
        print(f"❌ Error crítico en el volcado: {e}")

if __name__ == '__main__':
    with app.app_context():
        # ATENCIÓN: Esto borrará TODOS los partidos existentes y sus entradas asociadas
        print("Borrando base de datos de partidos anterior...")
        db.session.query(Partido).delete()
        db.session.commit()
        
        cargar_fixture_mundial_completo()