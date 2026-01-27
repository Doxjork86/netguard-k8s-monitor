import os
import time
from celery import Celery

# 1. Configuración de Celery usando variables de entorno
celery = Celery(
    'tasks',
    broker=os.environ.get('CELERY_BROKER_URL'),
    backend=os.environ.get('CELERY_RESULT_BACKEND')
)

# 2. Definimos una tarea "pesada"
# El decorador @celery.task permite que esta función vaya a Redis
@celery.task(bind=True)
def escanear_infraestructura(self, target_ip):
    """
    Simula un escaneo de red tipo Nmap que tarda 10 segundos.
    """
    self.update_state(state='PROGRESS', meta={'progress': 0, 'status': 'Iniciando...'})
    
    # Simulamos trabajo pesado (0% a 100%)
    total_steps = 5
    for i in range(total_steps):
        time.sleep(2) # Simula tiempo de procesamiento (2 seg por paso)
        progress = ((i + 1) / total_steps) * 100
        
        # Actualizamos el estado en Redis para que la API lo vea
        self.update_state(state='PROGRESS', meta={
            'progress': progress,
            'status': f'Escaneando puertos en {target_ip}...'
        })
    
    # Resultado final
    return {
        'status': 'Completado',
        'result': f'Puertos abiertos en {target_ip}: [22, 80, 443, 8080]',
        'vulnerabilities': 'Ninguna crítica detectada'
    }
