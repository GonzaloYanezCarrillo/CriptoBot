import requests
import time
import os
from keep_alive import keep_alive
from dotenv import load_dotenv
load_dotenv()
print("Cargando CriptoBot...")
url_webhook = os.getenv("DISCORD_WEBHOOK")
portafolio = [
    {"id": "bitcoin", "objetivo": 90000},
    {"id": "ethereum", "objetivo": 3000},
    {"id": "cardano", "objetivo": 3},
    {"id": "solana", "objetivo": 250},
]

# Diccionario de Logos (URLs de imágenes para cada moneda)
logos = {
    "bitcoin": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png",
    "ethereum": "https://assets.coingecko.com/coins/images/279/large/ethereum.png",
    "solana": "https://assets.coingecko.com/coins/images/4128/large/solana.png",
    "cardano": "https://assets.coingecko.com/coins/images/975/large/cardano.png"
}

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
    
keep_alive()
print("CriptoBot iniciado y en funcionamiento.")

while True:
    for moneda in portafolio:
        moneda_id = moneda["id"]
        precio_objetivo = moneda["objetivo"]
        precio = obtener_precio(moneda_id)
        if precio is None:
            continue
        print(f"El precio actual del {moneda_id} es: {precio} usd")
        if precio <= precio_objetivo:
            # Enviar alerta a Discord
            # Definir color según la moneda
            color_alerta = 5763719  # Verde
            data = {
                "username": "CryptoGonsalo 🤖",
                "embeds": [
                    {
                        "title": f"¡Oportunidad en {moneda_id.capitalize()}! 📉",
                        "description": f"El precio ha tocado tu zona de compra.",
                        "color": color_alerta,
                        "thumbnail": {
                            "url": logos.get(moneda_id, "") # Busca el logo, si no hay, lo deja vacío
                        },
                        "fields": [
                            {
                                "name": "💰 Precio Actual",
                                "value": f"**${precio:,.2f} USD**", # Formato con comas y negrita
                                "inline": True
                            },
                            {
                                "name": "🎯 Tu Objetivo",
                                "value": f"${precio_objetivo:,.2f} USD",
                                "inline": True
                            }
                        ],
                        "footer": {
                            "text": "Alerta automática • CryptoSentinel",
                            "icon_url": "https://cdn-icons-png.flaticon.com/512/1000/1000638.png"
                        },
                        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S') # Hora actual
                    }
                ]
            }
            try:    
                requests.post(url_webhook, json=data)
                print("Mensaje enviado al webhook de Discord.")

            except Exception as e:
                print(f"Error al obtener el precio: {e}")
    time.sleep(300)  # Esperar 300 segundos antes de la siguiente consulta