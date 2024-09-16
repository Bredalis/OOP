
class Camiseta:
	def __init__(self, talla, color, precio, marca):

		# Propiedades de las camisetas

		self.talla = talla
		self.color = color
		self.precio = precio
		self.marca = marca
		self.rebajada = False

	def crear_descuento(self, porcentaje): 
		self.precio = self.precio - self.precio * porcentaje / 100

		# Mostrar precio rebajado (descuento)

		if porcentaje < 100:
			self.rebajada = True

	def mostrar_informacion(self):

		info = f"\nDescripcion de la camiseta: \nMarca: {self.marca} \
		\nPrecio: {self.precio:.2f} \nColor: {self.color} \nTalla: {self.talla} \n"

		print(info)

		if self.rebajada != True:
			return "\nEste producto no esta rebajado"

		return "\nEste producto esta rebajado"

camisetas = [
	Camiseta("M", "Negro", 100, "Gucci"),
	Camiseta("M", "Rojo", 30, "Adidas")
]

for camisa in camisetas:
	print(camisa.mostrar_informacion())
	
	camisa.crear_descuento(50)
	print(camisa.mostrar_informacion())