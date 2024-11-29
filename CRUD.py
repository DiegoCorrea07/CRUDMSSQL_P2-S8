from CRUDProducto import CRUDProducto


class CRUD:
    def __init__(self, conexion):
        self.producto = CRUDProducto(conexion)

    def mostrar_opciones(self):
        print("\nOpciones CRUD:")
        print("1. Crear producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

    def ejecutar_opcion(self):
        while True:
            self.mostrar_opciones()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.producto.insertar()
            elif opcion == "2":
                self.producto.consultar()
            elif opcion == "3":
                self.producto.actualizar()
            elif opcion == "4":
                self.producto.eliminar()
            elif opcion == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, intente de nuevo.")


