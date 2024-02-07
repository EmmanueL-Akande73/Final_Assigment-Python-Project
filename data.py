class Shape:
    def area(self):
        pass

class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area (self):
        return 3.14 * self.radius**2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5* self.base * self.height
    
circle_unit = input("Put number to calculate circle area ");    
#creating objects of diffrents classes
circle = Circle(int(circle_unit))
triangle_height =input("put the triangles height ")
triangle_base =input("put the triangles base ")
triangle = Triangle (int(triangle_height),int(triangle_base))

#Accessing attributes and callinf the area() method
print("Area of Circle:", circle.area())
print("Area of Triangle:",triangle.area()) 