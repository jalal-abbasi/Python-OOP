class Circle:
    
    pi = 3.1416
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    # Add the method below this line
    def circle_area(self):
        return self.radius * self.radius * Circle.pi


        
blue_circle = Circle(15, "Blue")

# Call the method with blue_circle and assign the result to the variable final_area
final_area = blue_circle.circle_area()
print(final_area)




