class ElectronicDevice:

    def __init__(self, screen_size, voltage, amperage):
        self.screen_size = screen_size
        self.voltage = voltage
        self.amperage = amperage


class Computer(ElectronicDevice):

    def __init__(self, model, ram, cpu, graphics, screen_size, voltage, amperage):
        ElectronicDevice.__init__(self, screen_size, voltage, amperage)
        self.model = model
        self.ram = ram
        self.cpu = cpu
        self.graphics = graphics


class TV(ElectronicDevice):

    def __init__(self, volume_range, screen_type, screen_size, voltage, amperage):
        ElectronicDevice.__init__(self, screen_size, voltage, amperage)
        self.volume_range = volume_range
        self.screen_type = screen_type


class Desktop(Computer):
    def __init__(self, num_of_speaker, case_type, keyboard_type, model, ram, cpu, graphics, screen_size, voltage, amperage):
        Computer.__init__(self, model, ram, cpu, graphics, screen_size, voltage, amperage)
        self.num_of_speaker = num_of_speaker
        self.case_type = case_type
        self.keyboard_type = keyboard_type


class Laptop(Computer):
    def __init__(self, weight, keyboard_with_numlock, model, ram, cpu, graphics, screen_size, voltage, amperage):
        Computer.__init__(self, model, ram, cpu, graphics, screen_size, voltage, amperage)
        self.weight = weight
        self.keyboard_with_numlock = keyboard_with_numlock


my_laptop = Laptop(2.1, False, "lenovo", 8, 2.2, "Nvidia", 14, 100, 100)
print(my_laptop.weight)
print(my_laptop.graphics)


