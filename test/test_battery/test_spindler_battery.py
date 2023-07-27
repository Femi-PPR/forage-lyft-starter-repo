import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
	def test_needs_service_true(self):
		today = datetime.today().date()
		last_service_date = today.replace(year=today.year - 4)
		battery = SpindlerBattery(today, last_service_date)
		self.assertTrue(battery.needs_service())
		
	def test_needs_service_false(self):
		today = datetime.today().date()
		last_service_date = today.replace(year=today.year - 2)
		battery = SpindlerBattery(today, last_service_date)
		self.assertTrue(battery.needs_service())