import os
import sys
from inputReader import InputReader
from inputValidator import InputValidator
from solver import Solver

class ApplicationMgr():
	'''Klasa bedaca menadzerem aplikacji rozwiazujacej rownanie'''
	def __init__(self):
		if len( sys.argv) == 2:
			self.file = sys.argv[1]
		else:
			self.file = ""

	def solveEquation(self):
		if len(self.file) == 0:
			return None

		try:
			inReader = InputReader(self.file)
			inReader.readEquationsFromFile()

			inVal = InputValidator( inReader.equations )
			inVal.convertDataToFloat()

			self.solver = Solver(inVal)
			self.solver.solveEq()
			print('Rozwiazanie ukladu rownan:\n')
			print( self.solver.solution )
		except FileNotFoundError:
			print("This file does'n exist")

		except ValueError:
			print("Incorrect insert data (value)")

		# except Exception:
		# 	print("Incorrect insert data")


	def changeFile(self):
		self.file = input()

	def printMenu(self):
		print('\n\n\n-----------------------------------')
		print('File: '+appMgr.file)
		print('Press:')
		print('    1 - Solve equation')
		print('    2 - Change file')
		print('    3 - Draw chart')
		print('    4 - Exit')

	def drawChart(self):
		functionFile = open('function.dat','w')
		plotFile = open('plot.gp', 'w')
		functionFile.write(str(self.solver.solution[0])+" "+str(self.solver.solution[1]))

		plotFile.write("plot 'function.dat' with lines;")
		os.system('gnuplot plot.gp')
		os.remove('plot.gp')


if __name__=='__main__':
	appMgr = ApplicationMgr()

	chooseOperation = ""
	while 1:
		appMgr.printMenu()
		chooseOperation = input()

		if chooseOperation=='1':
			appMgr.solveEquation()
		elif chooseOperation=='2':
			appMgr.changeFile()
		elif chooseOperation=='3':
			appMgr.drawChart()
		else:
			print('Bye')
			sys.exit()



