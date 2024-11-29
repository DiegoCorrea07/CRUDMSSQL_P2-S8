from DBConnection import DBConnection
from CRUD import CRUD


def main():
    """
        Utilizando la Base de Datos del Proyecto Integrador.
        Desarrollar un programa funcional / Orientado a Objetos en Python 
        con conexión a SQL SERVER, con todas las Operaciones CRUD utilizando una Tabla seleccionada.

        Base de Datos: ProtoDEVDataBase en la Tabla Producto.

        Autores:
        - [Mathew Baquero.]
        - [Diego Correa.]
        - [Joel Ibarra.]

        Profesor: [Geovanni Aucancela Soliz.]
        Fecha: [29-11-2024]
        Materia: [Base de Datos II]
        NRC: [5560]

        Python: [3.11.10]
        pyodbc: [5.2.0]

    """

def main():
    db_connection = DBConnection()

    if db_connection.conexion:
        sistema_crud = CRUD(db_connection.conexion)
        sistema_crud.ejecutar_opcion()
        db_connection.cerrar()
    else:
        print("No se pudo establecer la conexión con la base de datos.")


if __name__ == "__main__":
    main()
