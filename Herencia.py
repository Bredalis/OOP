
class Persona:
	def __init__(self, nombre, edad, dni):
		self.nombre = nombre
		self.edad = edad
		self.dni = dni

	def mostrar_informacion(self):
		print(f"Nombre: {self.nombre}\nEdad: {self.edad}")

class Trabajador(Persona):
	def __init__(self, nombre, edad, dni, sueldo, cargo, empresa):
		super().__init__(nombre, edad, dni)
		self.sueldo = sueldo
		self.cargo = cargo
		self.empresa = empresa

	def calcular_sueldo(self):
		print(f"Sueldo: {12 * self.sueldo + 2000}")

# Ejemplo de uso
print("Información:\n")

oscar = Persona("Oscar", 23, "76893434")
oscar.mostrar_informacion()
print("DNI:", oscar.dni)

trabajador = Trabajador("Bredalis", 34, "564g98800", 21000, 
	"Programador", "Google")
trabajador.mostrar_informacion()
trabajador.calcular_sueldo()