
from abc import ABC, abstractmethod

class Personaje(ABC):
	@abstractmethod
	def __init__(self, nombre):
		self.nombre = nombre
		self.nivel = 0
		self.inventario = []
		self.vida = 100

	@abstractmethod
	def atacar(self, objetivo):
		pass

	@abstractmethod
	def estado(self):
		print(f"Nombre: {self.nombre}\nNivel: {self.nivel}")

	def subir_nivel(self):
		self.nivel += 1

	def obtener_inventario(self):
		print(f"Inventario de: {self.nombre}")
		for objeto in self.inventario:
			print(objeto)

class Mago(Personaje):
	def __init__(self, nombre):
		super().__init__(nombre)
		self.vida = 120
		self.inteligencia = 95
		self.inventario = ["Poción de Mana", "Grimorio"]

	def estado(self):
		print("Clase: Mago")
		super().estado()

	def atacar(self, objetivo):
		objetivo.vida -= self.inteligencia * 0.6
		print(f"Vida actual del objetivo es: {objetivo.vida}")

class Guerrero(Personaje):
	def __init__(self, nombre):
		super().__init__(nombre)
		self.vida = 200
		self.fuerza = 75
		self.inventario = ["Poción de vida", "Escudo", "Espada"]

	def estado(self):
		print("Clase: Guerrero")
		super().estado()

	def atacar(self, objetivo):
		objetivo.vida -= self.fuerza * 0.8
		print(f"El objetivo se ha quedado con {objetivo.vida} puntos de vida")

guerrero = Guerrero("Pedro")
mago = Mago("Yuto")

objetos = [guerrero, mago]

for personaje in objetos:
	personaje.estado()
	personaje.obtener_inventario()
	personaje.atacar(personaje)