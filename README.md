# Taller de FastAPI - Sistemas Operativos

Este proyecto es parte del taller de la materia de Sistemas Operativos en la Universidad EIA. Consiste en crear un servicio web utilizando FastAPI para manejar una base de datos cargada con datos seleccionados. El proyecto también se integra con NGROK para hacerlo accesible públicamente.

## Descripción del proyecto

El proyecto consiste en:
1. Selección y carga de un dataset en una base de datos (PostgreSQL).
2. Creación de un entorno virtual para manejar las dependencias del proyecto.
3. Desarrollo de endpoints con FastAPI para consultar y agregar datos en la base de datos.
4. Manejo de errores y excepciones en los endpoints.
5. Validación de los endpoints con scripts de prueba.
6. Integración de un archivo `.service` para asegurar que el servicio de FastAPI se inicie automáticamente.
7. Exposición del servicio a través de NGROK.

## Requisitos

Para correr este proyecto necesitarás:
- Python 3.10 o superior
- PostgreSQL instalado y configurado
- NGROK para exponer el servicio web
- Git para la gestión de versiones

## Instalación

1. Clona este repositorio:

    ```bash
    git clone git@github.com:SantiagoPA712/TallerFASTAPI.git
    cd TallerFASTAPI
    ```

2. Configura el entorno virtual:

    ```bash
    python3 -m venv env_wsl
    source env_wsl/bin/activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura tu base de datos PostgreSQL y carga el dataset usando el script `load_data.py`.

5. Ejecuta el servicio:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

6. Integra con NGROK para exponer el servicio:

    ```bash
    ngrok http 8000
    ```

## Uso

### Endpoints

- **GET** `/players/` - Consultar jugadores con opciones de paginación y filtros.
- **POST** `/players/` - Agregar nuevos jugadores a la base de datos.

Para ver la documentación completa, visita `/docs` en tu navegador cuando el servicio esté en funcionamiento.

## Scripts

### Test de Endpoints

Usa el script `test_endpoints.py` para validar el correcto funcionamiento de los endpoints:

```bash
python test_endpoints.py

Scripts de Bash
start_service.sh - Arranca el servicio de FastAPI automáticamente.
ngrok_setup.sh - Configura y arranca NGROK para exponer el servicio web.
Contribuciones
Las contribuciones a este proyecto son bienvenidas. Por favor, crea un issue para sugerencias de mejora o reportar errores.

Licencia
Este proyecto está licenciado bajo la Licencia MIT.
