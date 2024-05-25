
"""
Programa que muestra el sueldo 
de diferentes empleados
"""

class Empleado:
	def __init__(self, nombre, sueldo_mensual, numero, trabajo):
		self.nombre = nombre
		self.sueldo_mensual = sueldo_mensual
		self.numero = numero
		self.trabajo = trabajo

	def calcular_sueldo(self):
		sueldo = 12 * self.sueldo_mensual * (1 + self.numero / 100)
		print(f"El sueldo anual de {self.nombre} - {self.trabajo}, es de {sueldo}")

class Contable(Empleado):
	def __init__(self, nombre, sueldo_mensual, numero, trabajo):
		super().__init__(nombre, sueldo_mensual, numero, trabajo)

class Publicista(Empleado):
	def __init__(self, nombre, sueldo_mensual, numero, trabajo):
		super().__init__(nombre, sueldo_mensual, numero, trabajo)

empleados = [
	Empleado("Juan", 1000, 1, "empleado"),
	Contable("Juana", 2000, 4, "contable"),
	Publicista("Lucas", 1200, 5, "publicista")
]

for empleado in empleados:
	empleado.calcular_sueldo()