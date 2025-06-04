"""
Módulo para enviar mensajes a Slack mediante webhooks.
"""
import os
import requests

def send_message(webhook_url: str, mensaje: str) -> bool:
    """
    Envía un mensaje a un canal de Slack usando un webhook.
    
    Args:
        webhook_url: URL del webhook de Slack
        mensaje: Texto del mensaje a enviar
        
    Returns:
        bool: True si el mensaje se envió correctamente, False en caso de error
    """
    try:
        payload = {'text': mensaje}

        response = requests.post(
            webhook_url,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        return True

    except Exception as error:
        print(f"Error al enviar mensaje a Slack: {error}")
        return False

def get_env_value(env_var: str) -> str:
    """Obtiene un valor de configuración.
    
    Args:
        env_var: Nombre de la variable de entorno.
        
    Returns:
        El valor de configuración o None si no se encuentra.
    """

    env_value = os.getenv(env_var)
    if env_value is not None:
        return env_value
    else:
        return None