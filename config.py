import mariadb

# Configuración de conexión. Cámbialo por tus credenciales.
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "andrea",
    "password": "1234",
    "database": "CentroAdopcion"
}


def get_db_connection():
    try:
        conn = mariadb.connect(**DB_CONFIG)
        return conn
    except mariadb.Error as e:
        print(f"Error conectando a MariaDB: {e}")
        return None