# Add code to the init method to check that 
# * the type of center is a Coordinate obj and 
# * the type of radius is an int. 
# If either are not these types, raise a ValueError.
class Circle(object):
    def __init__(self, center, radius):

        self.center = center
        self.radius = radius
        

# center = Coordinate(2, 2)
# my_circle = Circle(center, 2)   # no error

# my_circle = Circle(2, 2)    # raises ValueError
# my_circle = Circle(center, 'two')  # raises ValueError
