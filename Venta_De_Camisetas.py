
class Camiseta:
    def __init__(self, talla, color, precio, marca):
        self.talla = talla
        self.color = color
        self.precio = precio
        self.marca = marca
        self.rebajada = False

    def crear_descuento(self, porcentaje):
        self.precio -= self.precio * porcentaje / 100

        # Establecer si el producto está rebajado
        if porcentaje < 100:
            self.rebajada = True

    def mostrar_informacion(self):
        info = (
            f"\nDescripción de la camiseta:\n"
            f"Marca: {self.marca}\n"
            f"Precio: {self.precio:.2f}\n"
            f"Color: {self.color}\n"
            f"Talla: {self.talla}\n"
        )

        print(info)

        if not self.rebajada:
            return "\nEste producto no está rebajado"
        return "\nEste producto está rebajado"

camisetas = [
    Camiseta("M", "Negro", 100, "Gucci"),
    Camiseta("M", "Rojo", 30, "Adidas")
]

for camisa in camisetas:
    print(camisa.mostrar_informacion())
    camisa.crear_descuento(50)
    print(camisa.mostrar_informacion())