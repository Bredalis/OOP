
class Camiseta:
	def __init__(self, talla, color, precio, marca):

		# Propiedades de las camisetas

		self.talla = talla
		self.color = color
		self.precio = precio
		self.marca = marca
		self.rebajada = False

	def descuento(self, porcentaje): 
		self.precio = self.precio - self.precio * porcentaje / 100

		# Mostrar precio rebajado (descuento)

		if porcentaje < 100:
			self.rebajada = True

	def informacion(self):

		info = f"\nDescripcion de la camiseta: \nMarca: {self.marca} \
		\nPrecio: {self.precio:.2f} \nColor: {self.color} \nTalla: {self.talla} \n"

		if self.rebajada != True:
			info += "\nEste producto no esta rebajado"
			return 

		info += "\nEste producto esta rebajado"
		return info

camisetas = [
	Camiseta("M", "Negro", 100, "Gucci"),
	Camiseta("M", "Rojo", 30, "Adidas")
]

for camisa in camisetas:
	camisa.descuento(20)
	camisa.descuento(50)

	print(camisa.informacion())
	print(camisa.informacion())