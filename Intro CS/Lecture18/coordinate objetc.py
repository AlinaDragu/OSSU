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