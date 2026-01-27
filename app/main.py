from flask import Flask, request, jsonify
from app.tasks import escanear_infraestructura
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "🚀 NetGuard Monitor Active"

# Endpoint 1: Solicitar una Tarea (POST)
@app.route('/api/scan', methods=['POST'])
def start_scan():
    content = request.json
    target_ip = content.get('ip', '127.0.0.1')
    
    # ¡AQUÍ ESTÁ LA MAGIA!
    # Usamos .delay() para enviar la tarea a Redis sin bloquear la API.
    task = escanear_infraestructura.delay(target_ip)
    
    return jsonify({
        "message": "Escaneo iniciado en segundo plano",
        "task_id": task.id,
        "status_url": f"/api/status/{task.id}"
    }), 202

# Endpoint 2: Consultar Estado (GET)
@app.route('/api/status/<task_id>', methods=['GET'])
def check_status(task_id):
    # Consultamos a Celery/Redis por el ID de la tarea
    task = escanear_infraestructura.AsyncResult(task_id)
    
    if task.state == 'PENDING':
        response = {'state': 'PENDING', 'progress': 0}
    elif task.state == 'PROGRESS':
        response = {
            'state': 'PROGRESS',
            'progress': task.info.get('progress', 0),
            'status': task.info.get('status', '')
        }
    elif task.state == 'SUCCESS':
        response = {
            'state': 'SUCCESS',
            'progress': 100,
            'result': task.result
        }
    else:
        response = {'state': task.state, 'error': str(task.info)}
        
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
