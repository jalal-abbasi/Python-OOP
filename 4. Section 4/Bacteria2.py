class Bacterium:
    # Complete the class
    def __init__(self, size, shape, x, y, multicellularity):
        self.size = size
        self.shape = shape
        self.x = x
        self.y = y
        self.multicelluarity = multicellularity


# Create 3 instances
thiomargarita_namibiensis = Bacterium(0.5, "spirilli", 0, 0, True)
epulopiscium = Bacterium(0.7, "bacili", 0, 1, False)
mycoplasma = Bacterium(0.3, 'cocci', 1, 0, False)

