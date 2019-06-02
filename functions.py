def hello():
    print('Hello' * 10)


def pyramid(layers):
    star = '#'
    for i in range(0, layers):
        print(star.center(layers * 2, ' '))
        star += '##'


def circle_area(radius):
    import math
    return math.pi * radius ** 2


def surface_area_cuboid(l, w, h):
    """This function takes length,width and height of cuboid and returns the surface area  """
    return 2 * (l * w + w * h + l * h)


hello()
pyramid(2)
print(circle_area(3))
print(surface_area_cuboid(3, 5, 7))
print(surface_area_cuboid.__doc__)
