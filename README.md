# 🛡️ NetGuard Monitor: Network Observability System

![Python](https://img.shields.io/badge/python-3.9-blue.svg?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?logo=kubernetes&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?logo=postgresql&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?logo=grafana&logoColor=white)

**NetGuard Monitor** es un sistema distribuido de monitoreo de red y análisis de rendimiento, diseñado para alta disponibilidad y resiliencia.

Este repositorio documenta la **evolución completa de la infraestructura**, demostrando la migración de un entorno de desarrollo local (Docker) hacia una arquitectura de producción orquestada (Kubernetes).

## 📂 Estructura del Proyecto

El repositorio contiene dos estrategias de despliegue que conviven para cubrir diferentes entornos del ciclo de vida de desarrollo:

| Componente | Archivo/Carpeta | Entorno Sugerido | Descripción |
| :--- | :--- | :--- | :--- |
| **Docker Compose** | `docker-compose.yml` | Desarrollo Local | Orquestación rápida para desarrollo y pruebas unitarias. |
| **Kubernetes** | `k8s/` | Producción | Despliegue escalable con **Self-Healing** y gestión de secretos. |
| **Código Fuente** | `app/` | Backend | API RESTful desarrollada en Python (Flask). |

## 🔄 Evolución de la Infraestructura

### Fase 1: Docker Compose (MVP)
Inicialmente, el sistema fue contenerizado para aislar dependencias y asegurar consistencia.
- **Stack:** Python API + Worker + Redis + PostgreSQL + Nginx.
- **Limitación:** La recuperación ante fallos dependía del reinicio manual o políticas simples del daemon.

### Fase 2: Migración a Kubernetes (Producción)
El sistema fue migrado a un clúster (Minikube) para obtener capacidades avanzadas de SRE.

**Mejoras Clave Implementadas:**
* **Resiliencia:** Uso de `Deployments` y `ReplicaSets` para garantizar alta disponibilidad.
* **Observabilidad:** Integración de **Prometheus y Grafana** para monitoreo de métricas de infraestructura en tiempo real.
* **Seguridad:** Gestión desacoplada de configuración mediante `ConfigMaps` y `Secrets`.
* **Networking:** Exposición de servicios mediante `NodePort` y ClusterIP.

## 📸 Evidencia (Observabilidad)

El clúster está instrumentado con un dashboard personalizado en Grafana para visualizar la salud de los nodos y el consumo de recursos de los pods.

![Grafana Dashboard]
<img width="1580" height="671" alt="grafana2" src="https://github.com/user-attachments/assets/4e34293e-dcf1-40c8-b9d3-eec3d4d43a8b" />

*(Panel de control mostrando métricas de CPU, Memoria y estado de los Pods)*

## 🚀 Guía de Inicio (Quick Start)

### Opción A: Docker (Local)
```bash
docker-compose up --build

### Opción B: Kubernetes (Producción)

# 1. Iniciar Minikube
minikube start

# 2. Aplicar manifiestos (Base de datos, Redis, API, Worker)
kubectl apply -f k8s/

# 3. Verificar estado de los pods
kubectl get pods

🛠️ Tecnologías
Lenguaje: Python 3.9 (Flask)

Base de Datos: PostgreSQL

Mensajería: Redis

Orquestador: Kubernetes v1.30+

Monitoring: Prometheus Operator & Grafana
