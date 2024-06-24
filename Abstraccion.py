
"""
La abstracción se refiere a la 
simplificación de objetos complejos 
al enfocarse solo en los detalles 
relevantes para el problema en cuestión. 
"""

from abc import ABC, abstractmethod

class Personaje(ABC):

	@abstractmethod
	def __init__(self, nombre):

		self.nombre = nombre
		self.nivel = 0
		self.inventario = []
		self.vida = 100

	@abstractmethod
	def atacar(self, objectivo):
		pass

	@abstractmethod
	def estado(self):
		print(f"Nombre: {self.nombre} \nNivel: {self.nivel}")

	def subir_nivel(self):
		self.nivel += 1

	def obtener_inventario(self):
		print(f"Inventario de: {self.nombre}")

		for objecto in self.inventario:
			print(objecto)

class Mago(Personaje):

	def __init__(self, nombre):
		super().__init__(nombre)

		self.vida = 120
		self.inteligencia = 95
		self.inventario = ["Pocion de Mana", "Grimorio"]

	def estado(self):
		print("Clase: Mago")
		super().estado()

	def atacar(self, objectivo):
		objectivo.vida -= self.inteligencia * 0.6
		print(f"Vida actual del objetivo es: {objectivo.vida}")

class Guerrero(Personaje):

	def __init__(self, nombre):
		super().__init__(nombre)

		self.vida = 200
		self.Fuerza = 75
		self.inventario = ["Pocion de vida", "Escudo", "Espada"]

	def estado(self):
		print("Clase: Guerrero")
		super().estado()

	def atacar(self, objectivo):
		objectivo.vida -= self.Fuerza * 0.8
		print(f"El objetivo se ha quedado con {objectivo.vida} puntos de vida")

guerrero = Guerrero("Pedro")
mago = Mago("Yuto")

objectos = [guerrero, mago]

for i in range(2):
	objectos[i].estado()
	objectos[i].obtener_inventario()
	objectos[i].atacar(objectos[i])