# Clase Padre: Producto 
# Define la clase base "Producto" con atributos y métodos comunes a todos los productos de la tienda.
class Producto:
    def __init__(self, nombre, precio, cantidad):
        # Atributos privados para encapsulamiento
        self._nombre = nombre  
        self._precio = precio  
        self._cantidad = cantidad  

    # Métodos getter y setter para el encapsulamiento de los atributos
    def obtener_nombre(self):
        return self._nombre

    def obtener_precio(self):
        return self._precio

    def obtener_cantidad(self):
        return self._cantidad

    def establecer_cantidad(self, cantidad):
        self._cantidad = cantidad

    # Muestra la información básica del producto
    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Precio: GS.{self._precio}, Stock: {self._cantidad}")

# Clase Hija: Ropa 
# Hereda de Producto y añade un atributo único "talla". Demuestra el uso de herencia.
class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        # Llama al constructor de Producto y agrega el atributo adicional "talla"
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def obtener_talla(self):
        return self._talla

# Clases Hijas de Ropa: Camisa, Pantalon, y Zapato
# Cada una hereda de "Ropa" y redefine el método "mostrar_info" para personalizar la salida.
class Camisa(Ropa):
    # Muestra información personalizada para Camisa
    def mostrar_info(self):  
        super().mostrar_info()
        print(f"Talla: {self._talla} (Camisa)")

class Pantalon(Ropa):
    # Muestra información personalizada para Pantalon
    def mostrar_info(self):  
        super().mostrar_info()
        print(f"Talla: {self._talla} (Pantalon)")

class Zapato(Ropa):
    # Constructor extendido con atributo adicional "tipo" y método "mostrar_info" personalizado
    def __init__(self, nombre, precio, cantidad, talla, tipo):
        super().__init__(nombre, precio, cantidad, talla)
        self._tipo = tipo

    def mostrar_info(self):  
        super().mostrar_info()
        print(f"Talla: {self._talla}, Tipo: {self._tipo} (Zapato)")

# Clase Inventario
# Almacena los productos en un inventario y los muestra; se usa como una abstracción de gestión de existencias.
class Inventario:
    def __init__(self):
        # Lista de productos en inventario
        self.prendas = []

    # Agrega productos a la lista del inventario
    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    # Muestra cada producto en inventario usando el método "mostrar_info" específico de cada producto
    def mostrar_inventario(self):
        for idx, prenda in enumerate(self.prendas, start=1):
            print(f"{idx}. ", end="")
            prenda.mostrar_info()
            print("-" * 20)
            
# Clase Carrito
# Permite al cliente seleccionar productos y ver un resumen de los artículos en su carrito
class Carrito:
    def __init__(self):
        # Lista de productos añadidos al carrito junto con su cantidad
        self.items = []

    # Agrega productos al carrito si hay suficiente stock
    def agregar_al_carrito(self, producto, cantidad):
        if cantidad <= producto.obtener_cantidad():
            self.items.append((producto, cantidad))
            producto.establecer_cantidad(producto.obtener_cantidad() - cantidad)
            print(f"----------Se agregaron {cantidad} unidades de {producto.obtener_nombre()} al carrito.----------")
        else:
            print("-----------Cantidad no disponible en stock.----------")

    # Muestra el resumen de la compra incluyendo el total
    def mostrar_resumen(self):
        total = 0
        print("Resumen de la compra:")
        for item, cantidad in self.items:
            subtotal = item.obtener_precio() * cantidad
            print(f"{item.obtener_nombre()} - Cantidad: {cantidad} - Subtotal: GS.{subtotal}")
            total += subtotal
        print(f"----------Total a pagar: GS.{total}-----------")

# Clase Tienda
# Representa el punto de interacción principal. Gestiona el inventario y las compras.
class Tienda:
    def __init__(self):
        # Inicializa un inventario y un carrito, y llena el inventario con productos
        self.inventario = Inventario()
        self.carrito = Carrito()
        self.poblar_inventario()

    # Agrega productos predefinidos al inventario
    def poblar_inventario(self):
        self.inventario.agregar_prenda(Camisa("Camisa de Hombre", 80000, 25, "M"))
        self.inventario.agregar_prenda(Camisa("Camisa de Mujer", 75000, 25, "S"))
        self.inventario.agregar_prenda(Ropa("Chaqueta de Hombre", 55000, 20, "M"))
        self.inventario.agregar_prenda(Ropa("Vestido de Mujer", 45000, 10, "P"))
        self.inventario.agregar_prenda(Pantalon("Pantalon de Hombre", 120000, 25, "L"))
        self.inventario.agregar_prenda(Pantalon("Pantalon de Mujer", 110000, 25, "M"))
        self.inventario.agregar_prenda(Zapato("Zapatos de Hombre", 200000, 25, "42", "Casual"))
        self.inventario.agregar_prenda(Zapato("Zapatos de Mujer", 150000, 25, "38", "Formal"))

    # Muestra el inventario de la tienda
    def mostrar_productos(self):
        print("----------Inventario de la tienda----------")
        self.inventario.mostrar_inventario()

    # Agrega productos al carrito, solicitando al usuario que seleccione productos del inventario
    def agregar_al_carrito(self):
        while True:
            self.mostrar_productos()
            try:
                opcion = int(input("Seleccione el numero del producto que desea agregar al carrito (0 para salir): "))
                if opcion == 0:
                    break
                producto = self.inventario.prendas[opcion - 1]
                cantidad = int(input(f"Ingrese la cantidad de '{producto.obtener_nombre()}' a comprar: "))
                self.carrito.agregar_al_carrito(producto, cantidad)
            except (IndexError, ValueError):
                print("*****Opción invalida.(tiene que ser del 1 al 8 o tambien 0 para salir) Intente nuevamente.*****")

    # Procesa la compra mostrando el resumen del carrito
    def procesar_compra(self):
        self.carrito.mostrar_resumen()

# Código principal para ejecutar la tienda
if __name__ == "__main__":
    tienda = Tienda()
    print("¡Bienvenido a la Tienda de Ropa!")
    
    tienda.agregar_al_carrito()
    tienda.procesar_compra()
