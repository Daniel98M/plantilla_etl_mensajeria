"""
Pruebas unitarias para el módulo de base de datos.
"""
import sys
sys.path.append('./')

import pandas as pd
import pandas.testing as tm

import pytest

from src.bd.base import DatabaseError, QueryError, InsertError

from tests.mocks.mocks_bd import MockDatabaseConnector

class TestDatabaseConnector:
    """Pruebas para la clase BaseDatabaseConnector."""

    @pytest.fixture
    def db_connector(self):
        """Fixture que devuelve una instancia de prueba de BaseDatabaseConnector."""
        return MockDatabaseConnector()

    def test_connect_disconnect(self, db_connector):
        """Prueba la conexión y desconexión de la base de datos."""
        # Verificar que inicialmente no hay conexión
        assert not db_connector.is_connected

        # Conectar y verificar
        db_connector.connect()
        assert db_connector.is_connected

        # Desconectar y verificar
        db_connector.disconnect()
        assert not db_connector.is_connected

    def test_connection_context_manager(self, db_connector):
        """Prueba el context manager de conexión."""
        with db_connector.connection() as conn:
            assert db_connector.is_connected
            assert conn is not None

        # Verificar que la conexión se cierra al salir del contexto
        assert not db_connector.is_connected

    def test_execute_get_query_success(self, db_connector):
        """Prueba exitosa de ejecución de consulta."""
        with db_connector.connection():
            result = db_connector.execute_get_query("SELECT * FROM test")
            assert isinstance(result, pd.DataFrame)
            assert len(result) == 3

    def test_execute_get_query_error(self, db_connector):
        """Prueba de error en ejecución de consulta."""
        with pytest.raises(QueryError, match="Error de consulta simulado"):
            with db_connector.connection():
                db_connector.execute_get_query("SELECT * FROM error")
                
    def test_execute_insert_df_success(self, db_connector):
        """Prueba exitosa de inserción de DataFrame."""
        df = pd.DataFrame({"col1": [1, 2], "col2": ["x", "y"]})
        with db_connector.connection():
            rows_inserted = db_connector.execute_insert_df(df, "test_table")
            assert rows_inserted == 2

    def test_execute_insert_df_error(self, db_connector):
        """Prueba de error en inserción de DataFrame."""
        df = pd.DataFrame({"col1": [1, 2], "col2": ["x", "y"]})
        with pytest.raises(InsertError):
            with db_connector.connection():
                db_connector.execute_insert_df(df, "error_table")


# Pruebas para las excepciones personalizadas
def test_database_error():
    """Prueba la excepción base DatabaseError."""
    with pytest.raises(DatabaseError):
        raise DatabaseError("Error de base de datos")


def test_query_error():
    """Prueba la excepción QueryError."""
    with pytest.raises(QueryError):
        raise QueryError("Error en consulta")


def test_insert_error():
    """Prueba la excepción InsertError."""
    with pytest.raises(InsertError):
        raise InsertError("Error en inserción")
