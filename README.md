# Sistema de Gestión de Entradas - Mundial de Fútbol 2026

<p align="center">
  <img src="https://img.shields.io/badge/Flask-v3.0+-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-v8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Bootstrap-v5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Python-v3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

---

## Descripción del Proyecto
Este proyecto corresponde al Parcial de Programación II para el IES 9-023[cite: 4, 28, 67]. [cite_start]Consiste en el desarrollo de una aplicación web temática responsive para la gestión y compra de entradas para el Mundial de Fútbol, integrando módulos de autenticación de usuarios, administración, partidos y servicios relacionados[cite: 4, 8, 19].

[cite_start]La aplicación aplica estrictamente los conceptos fundamentales de la Programación Orientada a Objetos (POO) como encapsulamiento, herencia, polimorfismo y abstracción mediante un sistema ORM (Flask-SQLAlchemy) conectado a una base de datos relacional[cite: 24, 29, 31].

---

## Arquitectura y Estructura del Código
[cite_start]El proyecto sigue un patrón modular y limpio, separando las responsabilidades en paquetes para mantener la mantenibilidad[cite: 32, 34]:

* **Entradas_Mundial/**: Paquete principal de la aplicación.
    * **controllers/**: Lógica de negocio y controladores (ej. `controller_autenticacion.py`).
    * **models/**: Modelos de SQLAlchemy para el mapeo POO y la Base de Datos.
        * `model_usuarios.py`: Implementación de herencia y polimorfismo de usuarios.
        * `model_partido.py`: Modelo para la gestión del fixture.
        * `model_compra.py` y `model_entradas.py`: Modelos de transacciones y tickets.
        * `model_actividad_turistica.py`: Gestión de servicios complementarios.
    * **routes/**: Blueprints de Flask para definir las rutas y endpoints del sistema.
        * `routes_autenticacion.py`, `routes_partidos.py`, `routes_compras.py`, `routes_turismo.py`.
    * **config.py**: Configuración de variables de entorno y conexión a MySQL.
    * **app.py**: Punto de entrada principal para ejecutar el servidor Flask.
* **.env**: Archivo local para credenciales críticas (excluido en Git).
* **README.md**: Documentación general del repositorio.

---

## Requisitos Obligatorios Implementados

### 1. Gestión de Usuarios y Seguridad
* [cite_start]**Registro de usuarios:** Permite el alta de nuevos perfiles en el sistema[cite: 12].
* **Inicio de sesión (Login):** Autenticación de usuarios mediante sesiones seguras[cite: 13].
* [cite_start]**Cierre de sesión (Logout):** Destrucción segura de la sesión activa para proteger la cuenta[cite: 15].
* [cite_start]**Páginas Protegidas:** Bloqueo de rutas específicas, accesibles únicamente para usuarios autenticados[cite: 14].
* **Roles Polimórficos (POO):** Mapeo en la base de datos para diferenciar entre los roles de Administrador y Usuario Cliente[cite: 16, 23].

### 2. Interfaz de Usuario
* [cite_start]Diseño moderno, intuitivo y completamente responsive implementando Bootstrap[cite: 18, 19].
* [cite_start]Identidad visual inmersiva enfocada en la estética de la Copa del Mundo[cite: 20].
* Estructura organizada con menús de navegación claros y vistas fluidas[cite: 21].

### 3. Base de Datos (MySQL)
* [cite_start]Persistencia relacional de datos utilizando el motor MySQL[cite: 24].
* [cite_start]Mapeo completo de las entidades principales del sistema mediante relaciones y claves foráneas[cite: 23].
* Operaciones CRUD que garantizan la correcta manipulación de la información disponible[cite: 25].

### Desafío Extra Opcional
* [cite_start]**Recuperación de Contraseña:** Flujo completo en la ruta `/recuperar-password` para restablecer el acceso de forma segura[cite: 63].

---

## Capturas de la Aplicación

<p align="center">
  <img src="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=800&q=80" alt="Vista de la Aplicación" width="80%">
</p>

---

## Instalación y Configuración Local

Sigan estos pasos para clonar el repositorio y levantar el servidor en modo desarrollo:

### 1. Clonar el repositorio
* `git clone https://github.com/ClaudioKody/ParcialProg2.git`
* `cd ParcialProg2`

### 2. Configurar el Entorno Virtual
* Crear entorno virtual: `python -m venv venv`
* Activar en Windows (PowerShell): `.\venv\Scripts\Activate.ps1`

### 3. Instalar Dependencias
* `pip install flask flask-sqlalchemy pymysql python-dotenv`

### 4. Configurar Variables de Entorno (.env)
Crear un archivo `.env` en la raíz del proyecto y rellenar con sus datos locales. 

* `MYSQL_HOST=localhost`
* `MYSQL_PORT=3306`
* `MYSQL_USER=root`
* `MYSQL_PASSWORD=tu_contraseña_aquí`
* `MYSQL_DB=mundial`

### 5. Ejecutar la Aplicación
Asegurate de tener el servicio de MySQL activo en tu máquina y ejecutá el módulo principal:
* `python -m Entradas_Mundial.app`

Al iniciar por primera vez, el sistema creará automáticamente todas las tablas en tu base de datos y dará de alta al Administrador oficial por defecto.

---

## Integrantes del Equipo
* Claudio Pérez
* Priscila Toledano
* Selene Quintero
* Tomás Naveda

---

## Criterios de Evaluación Cubiertos
* [cite_start]Registro, Login y Logout (15%) [cite: 52, 53]
* Página protegida (10%) [cite: 54, 55]
* [cite_start]Funcionalidad del módulo asignado (25%) [cite: 58, 60]
* [cite_start]Aplicación de POO (20%) [cite: 59]
* Diseño y uso de Bootstrap (10%) [cite: 59]
* [cite_start]Uso de Git y GitHub (10%) [cite: 59]
* [cite_start]Documentación y UML (10%) [cite: 59]

---
[cite_start]**Fecha de Entrega:** 22/06/2026 [cite: 68]  
[cite_start]**Docente:** Cristian Pietrobon [cite: 66]  
[cite_start]**Institución:** IES 9-023 [cite: 28, 69]