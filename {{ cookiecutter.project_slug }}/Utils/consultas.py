import pandas as pd
import numpy as np

import cx_Oracle
import sqlalchemy as sa

import yaml

# Variables globales
try:
    ruta_config = './config/config.yml'
    with open(ruta_config, "r") as archivo:
        config = yaml.safe_load(archivo)
except:
    ruta_config = '../config/config.yml'
    with open(ruta_config, "r") as archivo:
        config = yaml.safe_load(archivo)

# Variables para la conexión
ruta_instantclient = config['rutas']['ruta_instantclient']

dsn_con = config['credenciales']['dwh_cloud']['dsn_con']
usuario = config['credenciales']['dwh_cloud']['usuario']
password = config['credenciales']['dwh_cloud']['password']

# Conexión con la base de datos - CX_Oracle
cx_Oracle.init_oracle_client(lib_dir=ruta_instantclient)

conn = cx_Oracle.connect(user=f'{usuario}', password=f'{password}', dsn=dsn_con)
cur = conn.cursor()

# Funciones
def consulta(query):
    # Lectura del query
    df = pd.read_sql(query, con=conn)
    return(df)

def registro_to_dwh(df, query):
    # Convertir DataFrame a lista de tuplas con valores convertidos a str y truncados
    rows = [tuple(str(val)[:2000] for val in row) for row in df.values]

    total_rows = len(rows)
    chunksize = 5000

    # Inserción de los registros
    for i in range(0, total_rows, chunksize):
        chunk = rows[i:i+chunksize]
        cur.executemany(query, chunk)
        conn.commit()

def ejecutar_procedimiento(query):
    cur.callproc(query)
    conn.commit()

def ejecutar_procedimiento_parametros(query, parametros):
    cur.callproc(query, parametros)
    conn.commit()

def ejecutar_query(query):
    cur.execute(query)
    conn.commit()

def cerrar_conexion():
    # Cerramos la conexión
    conn.close()