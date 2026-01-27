# 🦅 NetGuard: Asynchronous Infrastructure Monitor

Plataforma de monitoreo de red no bloqueante diseñada para alta concurrencia. Utiliza una arquitectura orientada a eventos para procesar tareas pesadas en segundo plano sin afectar la experiencia del usuario.

## 🏗️ Arquitectura del Sistema

* **API Gateway (Nginx):** Reverse Proxy y terminación SSL.
* **Backend (Flask):** API RESTful que despacha tareas.
* **Message Broker (Redis):** Cola de mensajería en memoria para desacoplamiento total.
* **Workers (Celery):** Procesamiento distribuido de tareas pesadas (Escaneos, Backups).
* **Result Backend (PostgreSQL):** Persistencia de estados e históricos.

## 🚀 Stack Tecnológico
* **Docker Compose:** Orquestación de 5 microservicios.
* **Python 3.9:** Código unificado para API y Workers.
* **Redis & Celery:** Patrón Productor-Consumidor.

## ⚡ Cómo probarlo

1. Levantar el stack:
   ```bash
   docker compose up -d

2. Solicitar un escaneo (La API responde en milisegundos):
     `bash
   curl -X POST http://localhost/api/scan -H "Content-Type: application/json" -d '{"ip": "8.8.8.8"}'

3. Consultar estado (Polling):
      bash
   curl http://localhost/api/status/<TASK_ID>
