## EXAMPLE: simple Coordinate class
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def distance(self, other):
        """ Returns the euclidean distance between two Coordinate objects """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def to_origin(self):
        """ always sets self.x and self.y to 0,0 """
        self.x = 0
        self.y = 0
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"

# #Print a coordinate object's data attributes
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(f"c's x is {c.x} and origin's x is {origin.x}")

# #These are equivalent calls
print(c.distance(origin))
print(Coordinate.distance(c, origin))

# #Calling a new method
c.to_origin()
print(c.x, c.y)

# #Printing a coordinate object
print(c)
print(origin)
c+origin

