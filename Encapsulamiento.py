
"""
Programa que murestra 
el numero PI y calcula 
el perimetro, radio y 
area de un circulo
"""

class Circulo:
	def __init__(self, radio):

		# Propiedades

		self.__radio = radio
		self.__pi = 3.1415

	def calcular_perimetro(self):
		print(f"Perimetro: {2 * self.__pi * self.__radio}")

	def calcular_area(self):
		print(f"Area: {self.__pi * self.__radio ** 2}")

	def obtener_pi(self):
		print(f"PI: {self.__pi}")

	def obtener_radio(self, valor):
		self.__radio = valor

		# Si el valor no es positivo no se mostrara el radio

		try:
			if valor <= 0:
				return "No puede ser negativo ni cero"
		
			return f"Radio: {self.__radio}"

		except Exception as e:
			return f"Tiene que ser un numero positivo"		

print("Propiedades de un circulo:\n")

circulo = Circulo(2.5)

circulo.calcular_perimetro()
circulo.calcular_area()
circulo.obtener_pi()
print(circulo.obtener_radio(2))