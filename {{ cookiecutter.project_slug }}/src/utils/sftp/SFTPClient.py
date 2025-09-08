import paramiko

from src.utils.logger.logger import get_logger

class SFTPClient:
    def __init__(self, host, username, password, port=22, logger=None):
        self.logger = logger or get_logger(__name__)
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.transport = None
        self.sftp = None

    def __enter__(self):
        self.transport = paramiko.Transport((self.host, self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        self.logger.info(f"Conexión establecida a SFTP: {self.host}:{self.port}")
        return self.sftp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sftp: 
            self.sftp.close()
        if self.transport:
            self.transport.close()
        self.logger.info("Conexión SFTP cerrada")