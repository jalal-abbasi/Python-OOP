class Circle:
    pi = 3.1416
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color   
    def find_area(self) :
        return Circle.pi*self.radius*self.radius

blue_circle = Circle(5,"blue")
final_area = blue_circle.find_area()
print(final_area)
           