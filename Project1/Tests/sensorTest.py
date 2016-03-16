# from ..Application.sensor import Sensor

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__)[:-5], 'Application'))
# print( os.path.join(os.path.dirname(__file__)[:-5], 'Application') )
from sensor import Sensor
import unittest

class TestSensors(unittest.TestCase):
	'''Sensor class unit tests'''
	def setUp(self):
		self.sensors = []
		self.sensors.append( Sensor('Altimeter',None, None, 'feet') )
		self.sensors.append( Sensor('Fuel Tank', 0, 50, 'b') )
		self.sensors.append( Sensor('EngineTemp', -50, 150, 'C'))
		self.sensors.append( Sensor('OilTemp', -50, 150, 'C'))
		self.sensors.append( Sensor('Air Speed Indicator', 0, 500, 'knots'))
		self.sensors.append( Sensor('Pressure gauge', 0, 2000, 'hPa'))

	def test_correctAutoIncrementIDs(self):
		self.assertEqual( len(self.sensors), self.sensors[-1].id )












