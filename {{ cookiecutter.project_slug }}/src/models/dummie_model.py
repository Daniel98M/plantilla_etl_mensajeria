from src.utils.logger.logger import get_logger
from src.config.settings import DB_CONFIG

def dummie_model():
    """Run the dummie model."""
    logger = get_logger(__name__)
    logger.info('Dummie model')
    
    db_username = DB_CONFIG['user']
    db_password = DB_CONFIG['password']
    db_host = DB_CONFIG['host']
    db_name = DB_CONFIG['name']
    db_port = DB_CONFIG['port']

    print(db_username, db_password, db_host, db_name, db_port)  