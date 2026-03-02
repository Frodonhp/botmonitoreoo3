import os
import threading
import time
import requests
from flask import Flask

app = Flask(_name_)

# 1. SOLUCIÓN AL ERROR 501: Aceptar métodos GET y HEAD
@app.route('/', methods=['GET', 'HEAD'])
def home():
    return "Bot de Monitoreo O3 Activo y en Vivo 🚀", 200

# 2. SISTEMA ANTISUSPENSIÓN (Auto-Ping)
def keep_alive():
    url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}.onrender.com"
    while True:
        try:
            # Hace una petición a sí mismo cada 10 minutos
            requests.get(url)
            print("Ping enviado: Manteniendo el servicio despierto.")
        except Exception as e:
            print(f"Error en auto-ping: {e}")
        time.sleep(600) # 600 segundos = 10 minutos

def run_bot():
    """Aquí es donde iría la lógica original de Grass que creamos"""
    print("Iniciando lógica de recolección de puntos...")
    # Tu script de automatización de puntos aquí

if _name_ == "_main_":
    # Iniciar el hilo para mantener vivo el servicio
    if os.environ.get('RENDER_EXTERNAL_HOSTNAME'):
        threading.Thread(target=keep_alive, daemon=True).start()
    
    # Iniciar la lógica del bot en un hilo separado (opcional)
    # threading.Thread(target=run_bot, daemon=True).start()

    # Iniciar el servidor web en el puerto que pide Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
