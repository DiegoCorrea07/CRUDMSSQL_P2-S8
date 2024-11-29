class CRUDProducto:
    def __init__(self, conexion):
        self.conexion = conexion

    def consultar(self):
        """Consulta todos los registros de la tabla Producto."""
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT * FROM Producto"
            cursor.execute(consulta)
            resultados = cursor.fetchall()

            print("\nProductos en la base de datos:\n")
            for producto in resultados:
                print(f"ID: {producto.IdProducto}, Nombre: {producto.Nombre}, Descripción: {producto.Descripcion}, "
                      f"Precio: {producto.Precio}, SKU: {producto.SKU}, EstadoStock: {producto.EstadoStock}")
        except Exception as e:
            print("Error al consultar productos:", e)

    def insertar(self):
        """Inserta un nuevo producto en la tabla Producto."""
        try:
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            sku = input("Ingrese el SKU del producto: ")
            estado_stock = input("Ingrese el estado del stock: ")
            id_detalle_factura = input("Ingrese el ID del detalle de factura (o deje en blanco para NULL): ")
            id_oferta = input("Ingrese el ID de la oferta (o deje en blanco para NULL): ")

            cursor = self.conexion.cursor()
            consulta = """
                INSERT INTO Producto (Nombre, Descripcion, Precio, SKU, EstadoStock, IdDetalleFactura, IdOferta)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (
                nombre, descripcion, precio, sku, estado_stock,
                id_detalle_factura if id_detalle_factura else None,
                id_oferta if id_oferta else None
            ))
            self.conexion.commit()
            print("Producto insertado correctamente.")
        except Exception as e:
            print("Error al insertar producto:", e)

    def actualizar(self):
        """Actualiza un producto existente."""
        try:
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nombre = input("Ingrese el nuevo nombre del producto: ")
            descripcion = input("Ingrese la nueva descripción del producto: ")
            precio = float(input("Ingrese el nuevo precio del producto: "))
            sku = input("Ingrese el nuevo SKU del producto: ")
            estado_stock = input("Ingrese el nuevo estado del stock: ")

            cursor = self.conexion.cursor()
            consulta = """
                UPDATE Producto
                SET Nombre = ?, Descripcion = ?, Precio = ?, SKU = ?, EstadoStock = ?
                WHERE IdProducto = ?
            """
            cursor.execute(consulta, (nombre, descripcion, precio, sku, estado_stock, id_producto))
            self.conexion.commit()
            print("Producto actualizado correctamente.")
        except Exception as e:
            print("Error al actualizar producto:", e)

    def eliminar(self):
        """Elimina un producto por ID."""
        try:
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            cursor = self.conexion.cursor()
            consulta = "DELETE FROM Producto WHERE IdProducto = ?"
            cursor.execute(consulta, (id_producto,))
            self.conexion.commit()
            print("Producto eliminado correctamente.")
        except Exception as e:
            print("Error al eliminar producto:", e)
