# from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class CarFactory():

	@staticmethod
	def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
		return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date))

	@staticmethod
	def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
		return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date))

	@staticmethod
	def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
		return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(current_date, last_service_date))

	@staticmethod
	def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
		return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))

	@staticmethod
	def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
		return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))
		