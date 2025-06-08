"""
Unit tests for the Slack notifications module.
"""
from pathlib import Path
from typing import Any, Dict, Tuple
from unittest.mock import patch, Mock

import pytest
import requests

# Ensure the path is correctly configured
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.utils.notifications.slack import send_message
from tests.mocks.mocks_utils.mocks_slack import mock_success_response, mock_error_response, mock_webhook_url

class TestSlackNotifications:
    """Test class for Slack notifications."""

    @pytest.fixture
    def mock_webhook_url(self) -> str:
        """Mock webhook URL for testing."""
        return mock_webhook_url()

    @pytest.fixture
    def mock_success_response(self) -> Mock:
        """Mock successful response from Slack API."""
        return mock_success_response()

    @pytest.fixture
    def mock_error_response(self) -> Mock:
        """Mock error response from Slack API."""
        return mock_error_response()

    def test_send_message_success(self, mock_webhook_url: str, mock_success_response: Mock) -> None:
        """Test successful message sending to Slack."""
        mensaje = "Este es un mensaje de prueba"
        
        with patch('requests.post', return_value=mock_success_response) as mock_post:
            resultado = send_message(mock_webhook_url, mensaje)
            
            mock_post.assert_called_once()
            assert resultado is True
            
            # Verify requests.post was called with correct parameters
            args: Tuple[Any, ...]
            kwargs: Dict[str, Any]
            args, kwargs = mock_post.call_args
            assert kwargs['json'] == {'text': mensaje}
            assert kwargs['timeout'] == 10

    def test_send_message_http_error(self, mock_webhook_url: str, mock_error_response: Mock) -> None:
        """Test handling of HTTP errors when sending a message."""
        with patch('requests.post', return_value=mock_error_response):
            with patch('src.utils.notifications.slack.logger') as mock_logger:
                resultado = send_message(mock_webhook_url, "Mensaje con error")
                
                assert resultado is False
                mock_logger.error.assert_called_once()

    def test_send_message_connection_error(self, mock_webhook_url: str) -> None:
        """Test handling of connection errors."""
        with patch('requests.post', side_effect=requests.ConnectionError("Error de conexión")):
            with patch('src.utils.notifications.slack.logger') as mock_logger:
                resultado = send_message(mock_webhook_url, "Mensaje con error de conexión")
                
                assert resultado is False
                mock_logger.error.assert_called_once()

    def test_send_message_timeout(self, mock_webhook_url: str) -> None:
        """Test handling of request timeouts."""
        with patch('requests.post', side_effect=requests.Timeout("Timeout de la solicitud")):
            with patch('src.utils.notifications.slack.logger') as mock_logger:
                resultado = send_message(mock_webhook_url, "Mensaje con timeout")
                
                assert resultado is False
                mock_logger.error.assert_called_once()

    def test_send_message_empty_message(self, mock_webhook_url: str, mock_success_response: Mock) -> None:
        """Test sending an empty message."""
        with patch('requests.post', return_value=mock_success_response) as mock_post:
            resultado = send_message(mock_webhook_url, "")
            
            assert resultado is True
            mock_post.assert_called_once()
            args: Tuple[Any, ...]
            kwargs: Dict[str, Any]
            args, kwargs = mock_post.call_args
            assert kwargs['json'] == {'text': ''}

    def test_send_message_special_characters(self, mock_webhook_url: str, mock_success_response: Mock) -> None:
        """Test sending messages with special characters."""
        mensaje = "¡Mensaje con caracteres especiales: áéíóúñ¿?¡!"
        
        with patch('requests.post', return_value=mock_success_response) as mock_post:
            resultado = send_message(mock_webhook_url, mensaje)
            
            assert resultado is True
            args: Tuple[Any, ...]
            kwargs: Dict[str, Any]
            args, kwargs = mock_post.call_args
            assert kwargs['json'] == {'text': mensaje}
