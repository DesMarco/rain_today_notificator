# Rain Today Notificator ☔️

Este proyecto consulta el pronóstico del tiempo para una ubicación específica usando la API de OpenWeather. Si detecta lluvia en las próximas horas, envía un email de notificación para que no te olvides el paraguas.

## Cómo usar

1. Clona este repositorio.
2. Añade tus datos personales en el archivo `main.py`:
   - Tu latitud y longitud (`LAT` y `LONG`).
   - Tu API key de [OpenWeather](https://openweathermap.org/api).
   - Tus datos de email (correo remitente, destinatario y contraseña de aplicación Google).
3. Ejecuta `main.py`.

## Requisitos

- Python 3.x
- Librería requests (`pip install requests`)

## Nota

Debes generar una contraseña de aplicación en tu cuenta de Google para poder enviar emails vía SMTP con seguridad.

---

¡No olvides el paraguas! ☔️
