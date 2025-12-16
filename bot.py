import requests
import time
import os
from keep_alive import keep_alive
from dotenv import load_dotenv
load_dotenv()
print("Cargando CriptoBot...")
keep_alive()
print("CriptoBot iniciado y en funcionamiento.")
url_webhook = os.getenv("DISCORD_WEBHOOK")
portafolio = [
    {"id": "bitcoin", "objetivo": 90000},
    {"id": "ethereum", "objetivo": 3000},
    {"id": "cardano", "objetivo": 3},
    {"id": "solana", "objetivo": 250},
]

if not url_webhook:
    raise ValueError("La variable de entorno DISCORD_WEBHOOK no está definida.")


def obtener_precio(id_moneda):
    try:
        url_api = f"https://api.coingecko.com/api/v3/simple/price?ids={id_moneda}&vs_currencies=usd"
        respuesta = requests.get(url_api)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos[id_moneda]['usd']
    except Exception as e:
        print(f"Error al obtener el precio: {e}")
        return None
    
while True:
    for moneda in portafolio:
        moneda_id = moneda["id"]
        precio_objetivo = moneda["objetivo"]
        precio = obtener_precio(moneda_id)
        if precio is None:
            continue
        print(f"El precio actual del {moneda_id} es: {precio} usd")
        if precio <= precio_objetivo:
            mensaje = {
                "content": f"¡ALERTA! 🚨 {moneda_id.capitalize()} llegó a {precio} USD (Objetivo: {precio_objetivo})"
            }
            try:    
                requests.post(url_webhook, json=mensaje)
                print("Mensaje enviado al webhook de Discord.")

            except Exception as e:
                print(f"Error al obtener el precio: {e}")
    time.sleep(60)  # Esperar 60 segundos antes de la siguiente consulta