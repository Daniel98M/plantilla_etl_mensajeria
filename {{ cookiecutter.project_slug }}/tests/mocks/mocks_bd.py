"""
Mock de la clase DatabaseConnector.
"""

from typing import Dict, Optional
from contextlib import contextmanager

from unittest.mock import MagicMock

import pandas as pd

from src.bd.base import DatabaseConnector, DatabaseError, QueryError, InsertError

class MockDatabaseConnector(DatabaseConnector):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._connection = None

    def connect(self) -> None:
        """Establece la conexión simulada."""
        self._connection = MagicMock()
        return self._connection

    def disconnect(self) -> None:
        """Cierra la conexión simulada."""
        self._connection = None

    @property
    def is_connected(self) -> bool:
        """Verifica si hay una conexión activa."""
        return self._connection is not None

    @contextmanager
    def connection(self):
        """Context manager para manejo seguro de conexiones."""
        if not self.is_connected:
            self.connect()
        try:
            yield self._connection
        except Exception as e:
            self.logger.error("Error en la conexión: %s", str(e))
            # Si es una excepción específica de la base de datos, la dejamos pasar
            if isinstance(e, (DatabaseError, QueryError, InsertError)):
                raise
            # Para otras excepciones, lanzamos ConnectionError
            raise ConnectionError(f"Error de conexión: {str(e)}") from e
        finally:
            # Asegurarse de que la conexión se cierre al salir del contexto
            if self.is_connected:
                self.disconnect()

    def execute_get_query(
        self, query: str, params: Optional[Dict] = None
    ) -> pd.DataFrame:
        """Simula la ejecución de una consulta."""
        if "error" in query:
            raise QueryError("Error de consulta simulado")
        return pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})

    def execute_insert_df(
        self,
        df: pd.DataFrame,
        table_name: str,
        if_exists: str = "append",
        index: bool = False,
        chunksize: int = 1000,
        **kwargs,
    ) -> int:
        """Simula la inserción de datos."""
        if "error" in table_name:
            raise InsertError("Error de inserción simulado")
        return len(df)
