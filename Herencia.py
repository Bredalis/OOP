
"""
Uso de la Herencia de Jerarquia
en un ejemplo de ver el nombre, 
edad y dni de una persona y un trabajador
"""

class Persona:
	def __init__(self, nombre, edad, dni):

		# Propiedades

		self.nombre = nombre
		self.edad = edad
		self.dni = dni

	def mostrar_informacion(self):
		print(f"Nombre: {self.nombre} \nEdad: {self.edad}")

class Trabajador(Persona):

	# Hereda las propiedades de la clase persona
	
	def __init__(self, nombre, edad, dni, sueldo, cargo, empresa):
		super().__init__(nombre, edad, dni)

		self.sueldo = sueldo
		self.cargo = cargo
		self.empresa = empresa

	# Muestra el sueldo calculado

	def calcular_sueldo(self):
		print(f"Sueldo: {12 * self.sueldo + 2000}")

# Muestra los nombres, edades y dni

print("Informacion:\n")

oscar = Persona("Oscar", 23, "76893434")
oscar.mostrar_informacion()

print("dni:", oscar.dni)

trabajador = Trabajador("Bredalis", 34, 
	"564g98800", 21000, "Programador", "Google")

trabajador.mostrar_informacion()
trabajador.calcular_sueldo()