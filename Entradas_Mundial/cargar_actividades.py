from Entradas_Mundial.app import app
from Entradas_Mundial.models import db
from Entradas_Mundial.models.model_actividad_turistica import Concierto, ActividadRecreativa

def cargar_actividades():
    print(" Iniciando carga de actividades turísticas...")

    conciertos = [
        # Ciudad de México
        {"nombre": "Concierto Bad Bunny", "artista": "Bad Bunny", "descripcion": "El artista urbano más grande del mundo en vivo.", "ciudad": "Ciudad de México", "ubicacion": "Foro Sol, Ciudad de México", "estadio_recital": "Foro Sol", "precio_sugerido": 80.0},
        {"nombre": "Concierto Shakira", "artista": "Shakira", "descripcion": "La reina del pop latino en un show inolvidable.", "ciudad": "Ciudad de México", "ubicacion": "Estadio Azteca, Ciudad de México", "estadio_recital": "Estadio Azteca", "precio_sugerido": 90.0},

        # Guadalajara
        {"nombre": "Concierto Maluma", "artista": "Maluma", "descripcion": "Reggaeton y pop latino en su máxima expresión.", "ciudad": "Guadalajara", "ubicacion": "Arena VFG, Guadalajara", "estadio_recital": "Arena VFG", "precio_sugerido": 70.0},
        {"nombre": "Concierto Natalia Lafourcade", "artista": "Natalia Lafourcade", "descripcion": "Una noche de música mexicana única.", "ciudad": "Guadalajara", "ubicacion": "Teatro Degollado, Guadalajara", "estadio_recital": "Teatro Degollado", "precio_sugerido": 60.0},

        # Monterrey
        {"nombre": "Concierto J Balvin", "artista": "J Balvin", "descripcion": "El color del reggaeton en vivo.", "ciudad": "Monterrey", "ubicacion": "Arena Monterrey, Monterrey", "estadio_recital": "Arena Monterrey", "precio_sugerido": 75.0},

        # Toronto
        {"nombre": "Concierto Drake", "artista": "Drake", "descripcion": "El rey del rap canadiense en su ciudad.", "ciudad": "Toronto", "ubicacion": "Scotiabank Arena, Toronto", "estadio_recital": "Scotiabank Arena", "precio_sugerido": 120.0},
        {"nombre": "Concierto The Weeknd", "artista": "The Weeknd", "descripcion": "Una noche épica con el artista torontoniano.", "ciudad": "Toronto", "ubicacion": "Rogers Centre, Toronto", "estadio_recital": "Rogers Centre", "precio_sugerido": 130.0},

        # Vancouver
        {"nombre": "Concierto Nickelback", "artista": "Nickelback", "descripcion": "Rock canadiense en su máximo esplendor.", "ciudad": "Vancouver", "ubicacion": "Rogers Arena, Vancouver", "estadio_recital": "Rogers Arena", "precio_sugerido": 95.0},

        # Los Ángeles
        { "nombre": "Concierto Billie Eilish", "artista": "Billie Eilish", "descripcion": "La voz de una generación en vivo en LA.", "ciudad": "Los Ángeles", "ubicacion": "SoFi Stadium, Los Ángeles", "estadio_recital": "SoFi Stadium", "precio_sugerido": 110.0},
        {"nombre": "Concierto Kendrick Lamar", "artista": "Kendrick Lamar", "descripcion": "Hip hop de alto nivel desde Compton.", "ciudad": "Los Ángeles", "ubicacion": "Kia Forum, Los Ángeles", "estadio_recital": "Kia Forum", "precio_sugerido": 100.0},

        # Nueva York
        {"nombre": "Concierto Imagine Dragons", "artista": "Imagine Dragons", "descripcion": "Rock alternativo en el corazón de Nueva York.", "ciudad": "Nueva York", "ubicacion": "MetLife Stadium, Nueva York", "estadio_recital": "MetLife Stadium", "precio_sugerido": 115.0},
        {"nombre": "Concierto Coldplay", "artista": "Coldplay", "descripcion": "Una experiencia visual y musical única.", "ciudad": "Nueva York", "ubicacion": "Madison Square Garden, Nueva York", "estadio_recital": "Madison Square Garden", "precio_sugerido": 125.0},

        # Boston
        {"nombre": "Concierto Aerosmith", "artista": "Aerosmith", "descripcion": "Los legendarios rockeros de Boston.", "ciudad": "Boston", "ubicacion": "TD Garden, Boston", "estadio_recital": "TD Garden", "precio_sugerido": 105.0},

        # Dallas
        {"nombre": "Concierto Beyoncé", "artista": "Beyoncé", "descripcion": "La reina del pop en un espectáculo sin igual.", "ciudad": "Dallas", "ubicacion": "AT&T Stadium, Dallas", "estadio_recital": "AT&T Stadium", "precio_sugerido": 150.0},

        # Miami
        {"nombre": "Concierto Pitbull", "artista": "Pitbull", "descripcion": "Mr. Worldwide en su ciudad, Miami.", "ciudad": "Miami", "ubicacion": "Hard Rock Stadium, Miami", "estadio_recital": "Hard Rock Stadium", "precio_sugerido": 85.0},
        {"nombre": "Concierto Camila Cabello", "artista": "Camila Cabello", "descripcion": "Pop latino desde Miami para el mundo.", "ciudad": "Miami", "ubicacion": "Kaseya Center, Miami", "estadio_recital": "Kaseya Center", "precio_sugerido": 90.0},

        # Atlanta
        {"nombre": "Concierto Lil Jon", "artista": "Lil Jon", "descripcion": "Hip hop y crunk desde Atlanta.", "ciudad": "Atlanta", "ubicacion": "Mercedes-Benz Stadium, Atlanta", "estadio_recital": "Mercedes-Benz Stadium", "precio_sugerido": 80.0},

        # Houston
        {"nombre": "Concierto Travis Scott", "artista": "Travis Scott", "descripcion": "El fenómeno del trap en vivo.", "ciudad": "Houston", "ubicacion": "NRG Stadium, Houston", "estadio_recital": "NRG Stadium", "precio_sugerido": 95.0},

        # Filadelfia
        {"nombre": "Concierto Will Smith", "artista": "Will Smith", "descripcion": "El príncipe del rap de Filadelfia.", "ciudad": "Filadelfia", "ubicacion": "Lincoln Financial Field, Filadelfia", "estadio_recital": "Lincoln Financial Field", "precio_sugerido": 85.0},

        # Kansas City
        {"nombre": "Concierto country Kansas", "artista": "Luke Bryan", "descripcion": "Country music en el corazón de América.", "ciudad": "Kansas City", "ubicacion": "Arrowhead Stadium, Kansas City", "estadio_recital": "Arrowhead Stadium", "precio_sugerido": 70.0},

        # Seattle
        {"nombre": "Concierto Pearl Jam", "artista": "Pearl Jam", "descripcion": "Los íconos del grunge en su ciudad natal.", "ciudad": "Seattle", "ubicacion": "Lumen Field, Seattle", "estadio_recital": "Lumen Field", "precio_sugerido": 100.0},

        # San Francisco
        {"nombre": "Concierto Metallica", "artista": "Metallica", "descripcion": "El metal más legendario del mundo.", "ciudad": "San Francisco", "ubicacion": "Levi's Stadium, San Francisco", "estadio_recital": "Levi's Stadium", "precio_sugerido": 110.0},
    ]

    recreativas = [
        # Ciudad de México
        {"nombre": "Museo Nacional de Antropología", "descripcion": "El museo más importante de México con piezas arqueológicas únicas.", "ciudad": "Ciudad de México", "ubicacion": "Bosque de Chapultepec, Ciudad de México", "direccion_establecimiento": "Av. Paseo de la Reforma s/n", "horarios_disponibles": "Mar-Dom 9:00-19:00", "precio_sugerido": 15.0},
        {"nombre": "Recorrido por Teotihuacán", "descripcion": "Visitá las pirámides del Sol y la Luna, una maravilla del mundo antiguo.", "ciudad": "Ciudad de México", "ubicacion": "Teotihuacán, Estado de México", "direccion_establecimiento": "Zona Arqueológica de Teotihuacán", "horarios_disponibles": "Todos los días 9:00-17:00", "precio_sugerido": 20.0},

        # Guadalajara
        {"nombre": "Centro Histórico de Guadalajara", "descripcion": "Recorrido por la arquitectura colonial y la cultura tapatía.", "ciudad": "Guadalajara", "ubicacion": "Centro Histórico, Guadalajara", "direccion_establecimiento": "Plaza de Armas, Guadalajara", "horarios_disponibles": "Todos los días 8:00-20:00", "precio_sugerido": 0.0},
        {"nombre": "Tequila Tour", "descripcion": "Visitá la cuna del tequila y conocé su proceso de producción.", "ciudad": "Guadalajara", "ubicacion": "Tequila, Jalisco", "direccion_establecimiento": "Pueblo Mágico de Tequila", "horarios_disponibles": "Lun-Dom 10:00-18:00", "precio_sugerido": 35.0},

        # Monterrey
        {"nombre": "Parque Fundidora", "descripcion": "Parque recreativo en una antigua fundidora de acero.", "ciudad": "Monterrey", "ubicacion": "Parque Fundidora, Monterrey", "direccion_establecimiento": "Av. Fundidora 501", "horarios_disponibles": "Todos los días 6:00-22:00", "precio_sugerido": 0.0},

        # Toronto
        {"nombre": "Torre CN", "descripcion": "Una de las torres más altas del mundo con vista panorámica de Toronto.", "ciudad": "Toronto", "ubicacion": "290 Bremner Blvd, Toronto", "direccion_establecimiento": "290 Bremner Blvd", "horarios_disponibles": "Todos los días 9:00-22:00", "precio_sugerido": 40.0},
        {"nombre": "Mercado St. Lawrence", "descripcion": "El mercado más famoso de Toronto con gastronomía local.", "ciudad": "Toronto", "ubicacion": "92 Front St E, Toronto", "direccion_establecimiento": "92 Front St E", "horarios_disponibles": "Mar-Dom 8:00-18:00", "precio_sugerido": 0.0},

        # Vancouver
        {"nombre": "Stanley Park", "descripcion": "El parque urbano más grande de Canadá con senderos y playas.", "ciudad": "Vancouver", "ubicacion": "Stanley Park, Vancouver", "direccion_establecimiento": "Stanley Park Causeway", "horarios_disponibles": "Todos los días 6:00-22:00", "precio_sugerido": 0.0},

        # Los Ángeles
        {"nombre": "Universal Studios Hollywood", "descripcion": "El parque temático de cine más famoso del mundo.", "ciudad": "Los Ángeles", "ubicacion": "Universal City, Los Ángeles", "direccion_establecimiento": "100 Universal City Plaza", "horarios_disponibles": "Todos los días 9:00-20:00", "precio_sugerido": 109.0},
        {"nombre": "Paseo de la Fama de Hollywood", "descripcion": "Caminá sobre las estrellas de tus artistas favoritos.", "ciudad": "Los Ángeles", "ubicacion": "Hollywood Blvd, Los Ángeles", "direccion_establecimiento": "Hollywood Blvd & Vine St", "horarios_disponibles": "Todos los días, al aire libre", "precio_sugerido": 0.0},

        # Nueva York
        {"nombre": "Estatua de la Libertad", "descripcion": "El símbolo más icónico de los Estados Unidos.", "ciudad": "Nueva York", "ubicacion": "Liberty Island, Nueva York", "direccion_establecimiento": "Liberty Island", "horarios_disponibles": "Todos los días 9:00-17:00", "precio_sugerido": 25.0},
        {"nombre": "Central Park Tour", "descripcion": "Recorrido en bicicleta por el parque más famoso del mundo.", "ciudad": "Nueva York", "ubicacion": "Central Park, Nueva York", "direccion_establecimiento": "Central Park, Manhattan", "horarios_disponibles": "Todos los días 6:00-22:00", "precio_sugerido": 15.0},

        # Boston
        {"nombre": "Freedom Trail", "descripcion": "Recorrido histórico por los sitios más importantes de la revolución americana.", "ciudad": "Boston", "ubicacion": "Downtown Boston", "direccion_establecimiento": "Boston Common, Boston", "horarios_disponibles": "Todos los días 9:00-17:00", "precio_sugerido": 0.0},

        # Dallas
        {"nombre": "Sixth Floor Museum", "descripcion": "El museo dedicado al legado de John F. Kennedy.", "ciudad": "Dallas", "ubicacion": "411 Elm St, Dallas", "direccion_establecimiento": "411 Elm St", "horarios_disponibles": "Mar-Dom 10:00-18:00", "precio_sugerido": 18.0},

        # Miami
        {"nombre": "South Beach", "descripcion": "La playa más famosa de Miami con arte deco y ambiente único.", "ciudad": "Miami", "ubicacion": "South Beach, Miami", "direccion_establecimiento": "Ocean Drive, Miami Beach", "horarios_disponibles": "Todos los días, al aire libre", "precio_sugerido": 0.0},
        {"nombre": "Everglades Tour", "descripcion": "Navegá en airboat por los humedales más famosos de América.", "ciudad": "Miami", "ubicacion": "Everglades National Park, Florida", "direccion_establecimiento": "40001 State Road 9336", "horarios_disponibles": "Todos los días 9:00-17:00", "precio_sugerido": 45.0},

        # Atlanta
        {"nombre": "Acuario de Georgia", "descripcion": "Uno de los acuarios más grandes del mundo.", "ciudad": "Atlanta", "ubicacion": "225 Baker St NW, Atlanta", "direccion_establecimiento": "225 Baker St NW", "horarios_disponibles": "Todos los días 10:00-20:00", "precio_sugerido": 40.0},

        # Houston
        {"nombre": "Space Center Houston", "descripcion": "El centro espacial oficial de la NASA en Houston.", "ciudad": "Houston", "ubicacion": "1601 NASA Pkwy, Houston", "direccion_establecimiento": "1601 NASA Pkwy", "horarios_disponibles": "Todos los días 10:00-17:00", "precio_sugerido": 35.0},

        # Filadelfia
        {"nombre": "Independence Hall", "descripcion": "Donde se firmó la Declaración de Independencia de los EE.UU.", "ciudad": "Filadelfia", "ubicacion": "520 Chestnut St, Filadelfia", "direccion_establecimiento": "520 Chestnut St", "horarios_disponibles": "Todos los días 9:00-17:00", "precio_sugerido": 0.0},

        # Kansas City
        {"nombre": "National WWI Museum", "descripcion": "El museo más completo sobre la Primera Guerra Mundial.", "ciudad": "Kansas City", "ubicacion": "2 Memorial Dr, Kansas City", "direccion_establecimiento": "2 Memorial Dr", "horarios_disponibles": "Mar-Dom 10:00-17:00", "precio_sugerido": 20.0},

        # Seattle
        {"nombre": "Space Needle", "descripcion": "La torre icónica de Seattle con vista de 360 grados.", "ciudad": "Seattle", "ubicacion": "400 Broad St, Seattle", "direccion_establecimiento": "400 Broad St", "horarios_disponibles": "Todos los días 9:00-23:00", "precio_sugerido": 35.0},
        {"nombre": "Pike Place Market", "descripcion": "El mercado público más antiguo de los EE.UU., famoso por los vendedores de pescado.", "ciudad": "Seattle", "ubicacion": "Pike Place Market, Seattle", "direccion_establecimiento": "85 Pike St", "horarios_disponibles": "Lun-Sab 9:00-18:00", "precio_sugerido": 0.0},

        # San Francisco
        {"nombre": "Golden Gate Bridge Tour", "descripcion": "Recorrido a pie o en bici por el puente más famoso del mundo.", "ciudad": "San Francisco", "ubicacion": "Golden Gate Bridge, San Francisco", "direccion_establecimiento": "Golden Gate Bridge", "horarios_disponibles": "Todos los días, al aire libre", "precio_sugerido": 0.0},
        {"nombre": "Alcatraz Island", "descripcion": "Visitá la famosa prisión federal en la isla de Alcatraz.", "ciudad": "San Francisco", "ubicacion": "Alcatraz Island, San Francisco", "direccion_establecimiento": "Alcatraz Island", "horarios_disponibles": "Todos los días 9:00-18:00", "precio_sugerido": 45.0},
    ]

    contador = 0

    try:
        for c in conciertos:
            existe = Concierto.query.filter_by(nombre=c["nombre"], ciudad=c["ciudad"]).first()
            if not existe:
                nuevo = Concierto(
                    nombre=c["nombre"],
                    artista=c["artista"],
                    descripcion=c["descripcion"],
                    ciudad=c["ciudad"],
                    ubicacion=c["ubicacion"],
                    estadio_recital=c["estadio_recital"],
                    precio_sugerido=c["precio_sugerido"],
                    tipo_actividad="concierto"
                )
                db.session.add(nuevo)
                contador += 1

        for r in recreativas:
            existe = ActividadRecreativa.query.filter_by(nombre=r["nombre"], ciudad=r["ciudad"]).first()
            if not existe:
                nuevo = ActividadRecreativa(
                    nombre=r["nombre"],
                    descripcion=r["descripcion"],
                    ciudad=r["ciudad"],
                    ubicacion=r["ubicacion"],
                    direccion_establecimiento=r["direccion_establecimiento"],
                    horarios_disponibles=r["horarios_disponibles"],
                    precio_sugerido=r["precio_sugerido"],
                    tipo_actividad="actividad_recreativa"
                )
                db.session.add(nuevo)
                contador += 1

        db.session.commit()
        print (f"¡Éxito! Se cargaron { contador } actividades turísticas.")

    except Exception as e:
        db.session.rollback()
        print (f"Error: { e } " )

if __name__ == '__main__':
    with app.app_context():
        cargar_actividades()