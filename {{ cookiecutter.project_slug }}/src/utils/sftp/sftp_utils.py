import os
from typing import Optional
from src.utils.sftp.SFTPClient import SFTPClient


def upload_file_sftp(
    local_path: str,
    remote_path: str,
    sftp_client: SFTPClient,
    notify: Optional[callable] = None
):
    """
    Sube un archivo al servidor SFTP.
    """
    logger = sftp_client.logger

    if not os.path.exists(local_path):
        logger.error(f"Archivo no encontrado: {local_path}")
        raise FileNotFoundError(f"El archivo {local_path} no existe")

    with sftp_client as conn:
        conn.put(local_path, remote_path) 
        logger.info(f"Archivo {local_path} enviado a {remote_path}")

    if notify:
        notify(f"✅ Archivo enviado: {os.path.basename(local_path)}")


def download_file_sftp(
    remote_path: str,
    local_path: str,
    sftp_client: SFTPClient,
    notify: Optional[callable] = None
):
    """
    Descarga un archivo desde el servidor SFTP.
    """
    logger = sftp_client.logger

    with sftp_client as conn:
        conn.get(remote_path, local_path) 
        logger.info(f"Archivo {remote_path} descargado en {local_path}")

    if notify:
        notify(f"📥 Archivo descargado: {os.path.basename(local_path)}")