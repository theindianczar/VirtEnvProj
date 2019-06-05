import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        area = math.pi * self.radius ** 2
        return area

    def circumference_circle(self):
        circumference = 2 * math.pi * self.radius
        return circumference


while input('enter N to stop') != 'N':
    input_radius = int(input('enter circle radius'))
    circle1 = Circle(input_radius)
    print('circle area is', circle1.circle_area())
    print('circle circumference is', circle1.circumference_circle())
