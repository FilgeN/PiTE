'''0 1 2 3
   4 5 6 7'''

from inputReader import InputReader
from inputValidator import InputValidator

class Solver:
	''' Klasa rozwiazujaca rownanie  - nieskonczone obliczanie wyznacznikow '''
	def __init__(self, inValidator):
		self.inValidator = inValidator

	def solveEq(self):
		data = self.inValidator.data
		#DETerminant
		detMain = data[0][0]*data[1][1] - data[0][1]*data[1][0]
		detX = data[0][2]*data[1][1] - data[1][2]*data[0][1]
		detY =  data[1][2]*data[0][0] - data[0][2]*data[1][0]

		if detMain == detX and detX == detY:
			self.solution = "Uklad oznaczony"

		if detMain == 0 and detX != detY:
			self.solution = "Uklad nieoznaczony"

		self.solution = [detX/detMain, detY/detMain]



if __name__=='__main__':
	print('\n*****************')
	print('solver - selftest')
	inReader = InputReader('data.dat')
	inReader.readEquationsFromFile()


	inVal = InputValidator( inReader.equations )
	inVal.convertDataToFloat()

	solver = Solver(inVal)
	solver.solveEq()
	print('Rozwiazanie rownania:\n')
	print( solver.solution )

