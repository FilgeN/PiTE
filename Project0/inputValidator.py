from inputReader import InputReader

class InputValidator():
	''' Klasa sprawdzajaca czy zawartosc pliku ma sens '''
	def __init__(self, equations):
		self.__equations = equations

	def convertDataToFloat(self):
		'''Konwersja danych tekstowych na liczby
		   oraz sprawdzenie czy faktycznie sa liczbami'''
		self.data = []
		try:
			for equation in self.__equations:
				floatEquation = []
				for number in equation:
					floatEquation.append( float(number) )
				if len(floatEquation) != 3:
					raise InputDataError
				self.data.append(floatEquation)

		except ValueError:
			print('Wczytane dane zawieraja niepoprawne znaki!')\
			# sys.exit()
			raise ValueError

		except InputDataError:
			print('Bledna ilosc liczb.  [a b c] <-> [ax + by + c = 0')
			raise InputDataError


class InputDataError(Exception):
	def __init__(self):
		Exception.__init__(self)



if __name__=='__main__':
	inReader = InputReader('data.dat')
	inReader.readEquationsFromFile()

	inVal = InputValidator( inReader.equations )
	inVal.convertDataToFloat()

	assert( isinstance(inVal.data, list) )




