from datetime import datetime

from Utils.functions import config_logging

fecha = int(str(datetime.now()).replace('-', '')[:8])

def logging_decorator(func):
    logger = config_logging(fecha)
    
    def wrapper(*args, **kwargs):
        logger.info(f"Inicializando el script {func.__name__}.")
        try:
            func(*args, **kwargs)
            logger.info(f"{func.__name__} ejecutado con exito.")
        except Exception as e:
            logger.error(f"Ocurrio un error con el script: {func.__name__}.")
            logger.error(f"{e}")
            raise ValueError(f"Ha ocurrido un error: {func.__name__}: {e}")

    return wrapper
