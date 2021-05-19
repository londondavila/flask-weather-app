from .unit import Unit


class UnitConverter():

    # receive 
    def __init__(self, parser_default_unit, dest_unit=None):
        self.parser_default_unit = parser_default_unit
        self.dest_unit = dest_unit

        # define dict
        self._convert_functions = {
            Unit.CELSIUS: self.to_celsius,
            Unit.FAHRENHEIT: self.to_fahrenheit,
        }

    @property
    def dest_unit(self):
        return self.dest_unit

    @property
    def dest_unit(self, dest_unit):
        self.dest_unit = dest_unit

    def convert(self, temp):

        try:
            temperature = float(temp)
        except ValueError:
            return 0

        # check if desired unit is already in use or null
        if (self.dest_unit == self.parser_default_unit or self.dest_unit is None):
                return self.format_results(temperature)

        func = self.convert_functions(self.dest_unit)

        result = func(temperature)

        return self.format_results(result)

    # format output
    def format_results(self, value):
        return int(value) if value.is_integer() else f'{value:.1f}'

    # convert to celsius
    def to_celsius(self, fahrenheit_temp):
        converted_temp = (fahrenheit_temp - 32) * 5/9
        return converted_temp
    
    # convert to fahrenheit
    def to_fahrenheit(self, celsius_temp):
        converted_temp = (celsius_temp * 9/5) + 32
        return converted_temp