from tires.tires import Tires

class CarriganTires(Tires):
	def __init__(self, tire_wear):
		self.tire_wear = tire_wear

	def needs_service(self):
		return any(x >= 0.9 for x in self.tire_wear)
