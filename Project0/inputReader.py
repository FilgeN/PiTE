import sys

class InputReader():
	'''Klasa odpowiedzialna za wczytanie danych do pliku'''
	def __init__(self, file):
		self.file = open(file,'r')

	def readEquationsFromFile(self):
		'''Wczytanie rownan z pliku'''
		dataTmp = self.file.read().split('\n')

		'''Rozdzielenie rownan na parametry'''
		self.equations = []
		for equation in dataTmp:
			self.equations.append(equation.split())

