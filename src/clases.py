class Persona:
    def __init__(self, nombre, correo):
        self._nombre = nombre
        self._correo = correo

    def obtener_nombre(self):
        return self._nombre

    def obtener_correo(self):
        return self._correo

    def mostrar_datos(self):
        print("Nombre:", self._nombre)
        print("Correo:", self._correo)


class Empleado(Persona):
    def __init__(self, nombre, correo, cargo, sueldo):
        super().__init__(nombre, correo)
        self._cargo = cargo
        self._sueldo = sueldo

    def obtener_sueldo(self):
        return self._sueldo

    def asignar_sueldo(self, nuevo_sueldo):
        if nuevo_sueldo > 0:
            self._sueldo = nuevo_sueldo
        else:
            print("El sueldo no puede ser negativo o cero")

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Cargo:", self._cargo)
        print("Sueldo:", self._sueldo)


class Cliente(Persona):
    def __init__(self, nombre, correo, empresa):
        super().__init__(nombre, correo)
        self._empresa = empresa

    def obtener_empresa(self):
        return self._empresa

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Empresa:", self._empresa)


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def obtener_codigo(self):
        return self._codigo

    def obtener_nombre(self):
        return self._nombre

    def obtener_precio(self):
        return self._precio

    def obtener_stock(self):
        return self._stock

    def disminuir_stock(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero")
            return False
        if cantidad > self._stock:
            print("No hay stock suficiente para esta operacion")
            return False

        self._stock -= cantidad
        return True

    def mostrar_datos(self):
        print(f"Producto: {self._nombre} - Precio: ${self._precio} - Stock: {self._stock}")


class Pedido:
    def __init__(self, cliente, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        if cantidad > producto.obtener_stock():
            raise ValueError(
                f"No hay stock suficiente para este pedido. Stock disponible: {producto.obtener_stock()}"
            )

        self._cliente = cliente
        self._producto = producto
        self._cantidad = cantidad
        self._producto.disminuir_stock(self._cantidad)

    def calcular_total(self):
        return self._producto.obtener_precio() * self._cantidad

    def mostrar_resumen(self):
        print("Pedido de:", self._cliente.obtener_nombre())
        print("Producto:", self._producto.obtener_nombre())
        print("Cantidad:", self._cantidad)
        print("Total a pagar: $", self.calcular_total())