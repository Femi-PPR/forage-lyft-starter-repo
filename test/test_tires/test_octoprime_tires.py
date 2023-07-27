import unittest
from datetime import date

from tries.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
	def test_needs_service_true(self):
		tire_wear = [0.8, 0.8, 0.8, 0.8]
		tires = OctoprimeTires(tire_wear)
		self.assertTrue(tires.needs_service())

	def test_needs_service_false(self):
		tire_wear = [0.1, 0.3, 1, 0]
		tires = OctoprimeTires(tire_wear)
		self.assertTrue(tires.needs_service())