"""Test module for the logger configuration."""
import logging
from pathlib import Path

import pytest

# Ensure the path is correctly configured
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.utils.logger.logger import get_logger

# Configure the root logger for testing
logging.basicConfig(level=logging.WARNING)
logging.getLogger().handlers = []  # Limpiar manejadores existentes


def test_get_logger_returns_logger_instance():
    """Verify that get_logger returns a Logger instance with the correct name."""
    logger_name = "test_logger"
    logger = get_logger(logger_name)
    
    assert isinstance(logger, logging.Logger)
    assert logger.name == logger_name


def test_get_logger_with_none_returns_root_logger():
    """Verify that get_logger() without arguments returns the root logger."""
    logger = get_logger()
    assert logger is logging.getLogger()


def test_get_logger_raises_type_error_for_invalid_name():
    """Verify that get_logger validates the logger name type."""
    with pytest.raises(TypeError):
        get_logger(123)  # type: ignore


def test_get_logger_returns_same_instance_for_same_name():
    """
    Verify that get_logger implements the singleton pattern for the same name.
    
    Ensures multiple calls with the same name return the same instance.
    """
    logger1 = get_logger("test_same_instance")
    logger2 = get_logger("test_same_instance")
    assert logger1 is logger2
    
    # Clean up handlers to avoid side effects
    for handler in logger1.handlers[:]:
        if hasattr(handler, 'close'):
            handler.close()
        logger1.removeHandler(handler)

def test_logger_logs_messages_correctly(caplog):
    """
    Test basic message logging using caplog.
    
    Verifies that messages are correctly captured when using
    the appropriate log level.
    """
    logger_name = "test_logging"
    test_logger = logging.getLogger(logger_name)
    
    # Setup for log capture
    test_logger.handlers = []
    test_logger.propagate = True

    with caplog.at_level(logging.INFO, logger=logger_name):
        test_logger.info("Test message")

    assert "Test message" in caplog.text


def test_logger_handles_exceptions_correctly(caplog):
    """
    Test exception logging with full traceback.
    
    Verifies that both the error message and exception traceback
    are correctly logged.
    """
    test_logger = logging.getLogger("test_exception")
    test_logger.handlers = []
    test_logger.propagate = True

    with caplog.at_level(logging.ERROR, logger="test_exception"):
        try:
            raise ValueError("Test error")
        except ValueError:
            test_logger.exception("An error occurred")

    assert "An error occurred" in caplog.text
    assert "ValueError: Test error" in caplog.text


def test_logger_uses_correct_log_levels():
    """
    Test message filtering based on severity levels.
    
    Verifies that only messages with level equal or higher
    than the handler's configured level are logged.
    """
    test_logger = logging.getLogger("test_levels")
    test_logger.handlers = []
    
    # Configure an in-memory handler with WARNING level
    log_output = []
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARNING)
    handler.stream = type('mock', (), {'write': lambda s: log_output.append(s)})
    test_logger.addHandler(handler)
    
    test_logger.debug("Debug message")
    test_logger.warning("Warning message")
    
    assert "Debug message" not in "".join(log_output)
    assert "Warning message" in "".join(log_output)
    
    # Clean up resources
    test_logger.removeHandler(handler)
    handler.close()
