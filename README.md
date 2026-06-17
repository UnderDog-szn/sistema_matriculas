# Sistema de Matrículas - SMA

## Requisitos
- Python 3.12
- Django 5.2

## Instalación
pip install django==5.2

## Migraciones
python manage.py makemigrations
python manage.py migrate

# Ejecución
python manage.py runserver

# Acceso al admin
http://127.0.0.1:8000/admin

# Funcionalidades añadidas
- Formularios de registro para estudiantes, docentes y asignaturas.
- Vistas de listado de registros guardados para cada modelo.
- Enlaces directos desde las páginas de registro a las listas de objetos guardados.
- Bloques de vista rápida con los últimos registros insertados en cada formulario.
