# Sistema Web de Gestión de Inventario - DevOps

## Descripción del Proyecto
Este repositorio contiene la implementación práctica correspondiente a la evaluación y diagnóstico DevOps. El proyecto consiste en una API REST desarrollada para la gestión de inventario, diseñada específicamente para evidenciar la adopción de prácticas modernas de desarrollo de software, incluyendo Integración Continua (CI), Infraestructura como Código (IaC) y análisis estático de seguridad (SAST).

## Stack Tecnológico
* **Backend:** Python 3.9, FastAPI
* **Base de Datos:** PostgreSQL 13
* **Testing:** Pytest, HTTPX
* **Infraestructura:** Docker, Docker Compose
* **Automatización y Calidad:** GitHub Actions, SonarCloud

## Prácticas DevOps Implementadas

1. **Infraestructura como Código (Docker):** 
   Estandarización absoluta de los entornos de ejecución. La aplicación y su base de datos se despliegan de manera uniforme mediante un archivo `docker-compose.yml`, eliminando las dependencias manuales del sistema operativo anfitrión.

2. **Testing Automatizado:** 
   Validación de la lógica de negocio y endpoints a través de pruebas unitarias construidas con `pytest`, previniendo regresiones en el código base.

3. **Integración Continua (CI):** 
   Configuración de flujos de trabajo automatizados mediante GitHub Actions para la ejecución de pruebas e integración de código con cada confirmación en el repositorio.

4. **Inspección de Seguridad y Calidad (SAST):** 
   Integración con SonarCloud para la detección proactiva de vulnerabilidades, *code smells* y validación del *Quality Gate* antes de cualquier liberación a producción.

## Despliegue Local
Para inicializar la infraestructura en un entorno de desarrollo, asegúrese de contar con Docker Desktop en ejecución y utilice el siguiente comando en la terminal:

```bash
docker-compose up -d --build