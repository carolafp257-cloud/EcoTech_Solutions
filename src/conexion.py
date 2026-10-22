import oracledb


USUARIO = "C##ECOTECH_SOLUTIONS"
PASSWORD = "ecotech2026"
HOST = "192.168.56.1"
PUERTO = 1521
SID = "xe"

def obtener_conexion():
    """
    Establece y retorna una conexión segura con la base de datos Oracle
    utilizando la librería oficial oracledb.
    """
    try:
        dsn = oracledb.makedsn(HOST, PUERTO, sid=SID)
        conexion = oracledb.connect(
            user=USUARIO,
            password=PASSWORD,
            dsn=dsn
        )
        return conexion
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error de conexión Oracle [{error.code}]: {error.message}")
        return None