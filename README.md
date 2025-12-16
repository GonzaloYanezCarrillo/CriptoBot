# 📈 CryptoSentinel Bot

Un bot de automatización financiera desarrollado en Python que monitorea el mercado de criptomonedas 24/7 y envía alertas estratégicas en tiempo real a Discord.

**Estado:** 🟢 En vivo (Desplegado en Render)

## 💡 Descripción
Este proyecto nace de la necesidad de automatizar el seguimiento de precios de activos volátiles. En lugar de revisar gráficos manualmente, el bot consulta la API de CoinGecko periódicamente y utiliza Webhooks para notificar oportunidades de compra o venta basadas en objetivos predefinidos.

## 🚀 Funcionalidades Principales
- **Arquitectura Escalable:** Diseño modular que permite agregar nuevas monedas al portafolio simplemente editando una lista de configuración.
- **Notificaciones Push:** Integración con Discord vía Webhooks para alertas instantáneas.
- **Resiliencia:** Sistema de manejo de errores (`try/except`) y reconexión automática ante fallos de red.
- **Seguridad:** Manejo de credenciales sensibles mediante Variables de Entorno (`.env`).
- **Cloud-Native:** Configurado con un servidor Flask ligero para mantenerse activo (Keep-Alive) en entornos de nube como Render.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.10+
- **Datos:** CoinGecko API
- **Comunicación:** Discord Webhooks
- **Servidor Web:** Flask & Gunicorn
- **Infraestructura:** Render (Cloud PaaS) + UptimeRobot (Monitoreo)