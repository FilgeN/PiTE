from applicationMgr import ApplicationMgr
from inputReader import InputReader
from inputValidator import InputValidator
from inputValidator import InputDataError
from solver import Solver
from io import IOBase

import unittest

class TestInputReader(unittest.TestCase):
	'''Testy jednostkowe klasy InputReader'''

	def setUp(self):
		self.inReader = InputReader('data.dat')

	def test_readData(self):
		self.inReader.readEquationsFromFile()
		self.assertIsInstance( self.inReader.file, IOBase )
		self.assertNotIsInstance( self.inReader.file, str)
		self.assertNotIsInstance( self.inReader.file, list)

	def test_notFileRaiseException(self):
		with self.assertRaises(FileNotFoundError):
			InputReader('doesntExistingFile')

	def tearDown(self):
		self.inReader.file.close()


class TestInputValidator(unittest.TestCase):
	'''Testy jednostkowe klasy InputValidator'''
	def setUp(self):
		self.inReader = InputReader('data.dat')
		self.inReader2 = InputReader('incorrectData.dat')
		self.inReader3 = InputReader('incorrectData2.dat')
		self.inReader4 = InputReader('incorrectData3.dat')

		self.inReader.readEquationsFromFile()
		self.inReader2.readEquationsFromFile()
		self.inReader3.readEquationsFromFile()
		self.inReader4.readEquationsFromFile()

		self.inValidator = InputValidator(self.inReader.equations)
		self.inValidator2 = InputValidator(self.inReader2.equations)
		self.inValidator3 = InputValidator(self.inReader3.equations)
		self.inValidator4 = InputValidator(self.inReader4.equations)

	def test_inputDataContainsCorrectChars(self):
		self.inValidator.convertDataToFloat()
		self.assertIsInstance( self.inValidator.data, list)

	def test_inputDataContainsIncorrectChars(self):
		with self.assertRaises(ValueError):
			self.inValidator2.convertDataToFloat()

	def test_inputDataContainsCorrectAmountOfEquations(self):
		self.inValidator.convertDataToFloat()
		self.assertGreater( len(self.inValidator.data), 1 )

	def test_inputDataContainsIncorrectAmountOfEquations(self):
		self.inValidator3.convertDataToFloat()
		self.assertLess( len(self.inValidator3.data), 2 )

	def test_inputDataContainsCorrectAmountOfNumbers(self):
		self.inValidator.convertDataToFloat()
		for equation in self.inValidator.data:
			self.assertEqual( len(equation), 3 )

	def test_inputDataContainsIncorrectAmountOfNumbers(self):
		with self.assertRaises(InputDataError):
			self.inValidator4.convertDataToFloat()
			print(self.inValidator4.data)

	def tearDown(self):
		self.inReader.file.close()
		self.inReader2.file.close()
		self.inReader3.file.close()
		self.inReader4.file.close()

class TestSolver(unittest.TestCase):
	'''Zaimplementowac testy solvera!!!'''
	pass



if __name__ == '__main__':
	print('Main:\n')
	unittest.main()

