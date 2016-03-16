from sensor import Sensor
import sys

class FlightRecorder:
	'''Klasa bedaca menadzerem rejestratora lotu'''
	def __init__(self):
		# obiekt polaczenia z baza danych
		# obiekt pilota
		pass

	def signIn(self):
		pass

	def signOut(self):
		pass

	def initSensors(self):
		#Sensor(name, min, max)
		self.sensors = []
		self.sensors.append( Sensor('Altimeter',None, None, 'feet') )
		self.sensors.append( Sensor('Fuel Tank', 0, 50, 'b') )
		self.sensors.append( Sensor('EngineTemp', -50, 150, 'C'))
		self.sensors.append( Sensor('OilTemp', -50, 150, 'C'))
		self.sensors.append( Sensor('Air Speed Indicator', 0, 500, 'knots'))
		self.sensors.append( Sensor('Pressure gauge', 0, 2000, 'hPa'))


	def readSensors(self):
		pass

	def setFlightRoute(self):
		pass

	def flightStart(self):
		pass

	def flightEnd(self):
		pass

if __name__ == '__main__':
	while(True):
		print("blabla")
		print("blabla")
		print("blabla")
		print("blabla2")
		sys.exit(1)
