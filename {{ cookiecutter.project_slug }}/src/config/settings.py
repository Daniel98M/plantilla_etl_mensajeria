"""Configuración general del proyecto."""
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env si existe
load_dotenv()

# Configuración general
class Settings:
    """Configuración general del proyecto."""

    # Entorno
    ENV: str = os.getenv("ENV", "development")  # development, production, test

    # Base de datos
    DB_USER: str = os.getenv("DB_USER", "user")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_NAME: str = os.getenv("DB_NAME", "my_database")
    DB_PORT: int = int(os.getenv("DB_PORT", '5432'))

    # API keys
    API_URL: str = os.getenv("API_URL", "")
    API_KEY: str = os.getenv("API_KEY", "")

    # Rutas
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    MODELS_DIR = os.path.join(BASE_DIR, "models")
    LOGS_DIR = os.path.join(BASE_DIR, "logs")

    # Parámetros para modelos (ejemplo)
    RANDOM_SEED = 13
    TEST_SIZE = 0.2
    
settings = Settings()
