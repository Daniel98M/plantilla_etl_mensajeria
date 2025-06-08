""" Mocks para el módulo de notificaciones de Slack. """
from unittest.mock import MagicMock
import requests

def mock_success_response():
    """Respuesta exitosa simulada de la API de Slack."""
    response = MagicMock()
    response.status_code = 200
    response.raise_for_status.return_value = None
    return response

def mock_error_response():
    """Respuesta de error simulada de la API de Slack."""
    response = MagicMock()
    response.status_code = 400
    response.raise_for_status.side_effect = requests.HTTPError("Error de solicitud")
    return response

def mock_webhook_url():
    """URL de webhook de prueba."""
    return "https://hooks.slack.com/services/TEST/TOKEN"
