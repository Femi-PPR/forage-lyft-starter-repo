from abc import ABC

from engine import Engine


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return self.warning_light_is_on
