
class Circulo:
	def __init__(self, radio):
		self.__radio = radio
		self.__pi = 3.1415

	def calcular_perimetro(self):
		print(f"Perímetro: {2 * self.__pi * self.__radio}")

	def calcular_area(self):
		print(f"Área: {self.__pi * self.__radio ** 2}")

	def obtener_pi(self):
		print(f"PI: {self.__pi}")

	def obtener_radio(self, valor):
		try:
			if valor <= 0:
				return "No puede ser negativo ni cero"

			self.__radio = valor	
			return f"Radio: {self.__radio}"

		except Exception as e:
			print(f"Error inesperado: {e}")

print("Propiedades de un círculo:\n")

circulo = Circulo(2.5)

circulo.calcular_perimetro()
circulo.calcular_area()
circulo.obtener_pi()
print(circulo.obtener_radio(2))