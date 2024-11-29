import pyodbc
import json


class DBConnection:
    def __init__(self):
        config = self.cargar_credenciales()
        self.server = config["server"]
        self.database = config["database"]
        self.username = config["username"]
        self.password = config["password"]
        self.connection_string = f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        self.conexion = None
        self.conectar()

    def cargar_credenciales(self):
        """Carga las credenciales desde el archivo JSON."""
        try:
            with open("config.json", "r") as file:
                return json.load(file)
        except Exception as e:
            print("Error al cargar credenciales:", e)
            return None

    def conectar(self):
        """Establece conexión con la base de datos."""
        try:
            self.conexion = pyodbc.connect(self.connection_string)
            print("Conexión exitosa a la base de datos.")
        except Exception as e:
            print("Error al conectar:", e)
            self.conexion = None

    def cerrar(self):
        """Cierra la conexión."""
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")
