# Sistema de Gestión de Entradas - Mundial de Fútbol 2026

<p align="center">
  <img src="https://img.shields.io/badge/Flask-v3.0+-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-v8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Bootstrap-v5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Python-v3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

---

## Descripción del Proyecto
Este proyecto corresponde al Parcial de Programación II para el IES 9-023. Consiste en el desarrollo de una aplicación web temática responsive para la gestión y compra de entradas para el Mundial de Fútbol, integrando módulos de autenticación de usuarios, administración, partidos y servicios relacionados.

La aplicación aplica estrictamente los conceptos fundamentales de la Programación Orientada a Objetos (POO) como encapsulamiento, herencia, polimorfismo y abstracción mediante un sistema ORM (Flask-SQLAlchemy) conectado a una base de datos relacional.

---

## Arquitectura y Estructura del Código
El proyecto sigue un patrón modular y limpio, separando las responsabilidades en paquetes para mantener la mantenibilidad:

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
* **Registro de usuarios:** Permite el alta de nuevos perfiles en el sistema.
* **Inicio de sesión (Login):** Autenticación de usuarios mediante sesiones seguras.
* **Cierre de sesión (Logout):** Destrucción segura de la sesión activa para proteger la cuenta.
* **Páginas Protegidas:** Bloqueo de rutas específicas, accesibles únicamente para usuarios autenticados.
* **Roles Polimórficos (POO):** Mapeo en la base de datos para diferenciar entre los roles de Administrador y Usuario Cliente.

### 2. Interfaz de Usuario
* Diseño moderno, intuitivo y completamente responsive implementando Bootstrap.
* Identidad visual inmersiva enfocada en la estética de la Copa del Mundo.
* Estructura organizada con menús de navegación claros y vistas fluidas

### 3. Base de Datos (MySQL)
* Persistencia relacional de datos utilizando el motor MySQL
* Mapeo completo de las entidades principales del sistema mediante relaciones y claves foráneas
* Operaciones CRUD que garantizan la correcta manipulación de la información disponible

### Desafío Extra Opcional
**Recuperación de Contraseña:** Flujo completo en la ruta `/recuperar-password` para restablecer el acceso de forma segura.

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
* Claudio Pérez         (Rama Kody)
* Priscila Toledano     (Rama priscila)
* Selene Quintero       (Rama Selene)
* Tomás Naveda          (Rama Shelby)

---
**Fecha de Entrega:** 22/06/2026  
**Docente:** Cristian Pietrobon  
**Institución:** IES 9-023 
