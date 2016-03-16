


class Sensor:
	__idCounter = 0
	def __init__(self, name, min, max, units):
		Sensor.__idCounter += 1
		self.id = Sensor.__idCounter
		self.name = name
		self.min = min
		self.max = max
		self.units = units
		self.value = 0

	def getValue(self):
		return self.value

	def setValue(self, newValue):
		self.value = newValue

