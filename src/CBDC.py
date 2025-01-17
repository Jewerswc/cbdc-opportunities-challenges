# Class representing Central Bank Digital Currency

class CBDC:
    def __init__(self, name, value, country):
        self.name = name
        self.value = value
        self.country = country

    def __str__(self):
        return f'{self.name} ({self.country}): {self.value}'