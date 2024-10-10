class Celsius:
    def __init__(self, temperature=0):
        # During initialization, the setter is called to set the temperature
        self.temperature = temperature

    def to_fahrenheit(self):
        # Convert the temperature to Fahrenheit
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        # Getter for the temperature property
        print("Getting Value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        # Setter for the temperature property with a validation check
        print("Setting Value....")
        if value < -275:
            raise ValueError("Temperature below -275 is not valid!")
        self._temperature = value


# Example usage
human = Celsius(37)  # Calls the setter to set the temperature
print(human.temperature)  # Calls the getter to retrieve the temperature
print(human.to_fahrenheit())  # Converts to Fahrenheit and prints the result