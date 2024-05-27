
from random import randint

class Tragamonedas:

	def __init__(self, id, premio):

		self.id = id
		self.premio = premio
		self.monedas = 0
		self.jackpots = 0 

	def __str__(self):
		return "id: " + str(self.id) + " - premio: " + str(self.premio)

	def __eq__(self, Otro):
		return self.monedas == Otro.monedas

	def __lt__(self, Otro):
		return self.monedas < Otro.monedas

	def __gt__(self, Otro):
		return self.monedas > Otro.monedas

	def jugar(self):
		
		self.monedas += 1
		
		numeros = randint(0, 9), randint(0, 9), randint(0, 9)
		mensaje = ""

		if numeros[0] == numeros[1] == numeros[2]:

			self.jackpots += 1
			mensaje = f"Ganaste {self.premio}"

		else:
			mensaje = "Mejor suerte para la proxima"

		return numeros, mensaje

jugador_1 = Tragamonedas("1", "20000$")
jugador_2 = Tragamonedas("1", "20000$")

print(jugador_1)
print(jugador_1.id == jugador_2.id)

for i in range(100):	
	print(jugador_1.jugar(), i)