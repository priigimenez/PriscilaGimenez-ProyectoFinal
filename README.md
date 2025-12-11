# Data Governance Blog

Este proyecto es un blog desarrollado en Django para compartir artículos, ideas y recursos sobre Data Governance.

## Características
- Publicación de posts sobre temas de gobierno de datos
- Creación y gestión de categorías y etiquetas relacionadas con Data Governance
- Interfaz web sencilla y moderna

## Instalación
1. Clona el repositorio:
   ```
   git clone https://github.com/priigimenez/Python87370-ProyectoDataGovernance.git
   ```
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Ejecuta el servidor:
   ```
   python manage.py runserver
   ```

## Uso
- Accede a `/posts/` para crear y ver publicaciones.
- Accede a `/categorias/nueva/` para crear nuevas categorías.
- Accede a `/etiquetas/nueva/` para crear nuevas etiquetas.

## Tecnologías
- Python 3
- Django
- Bootstrap (para el diseño)

## Licencia
Este proyecto está bajo la licencia MIT.
