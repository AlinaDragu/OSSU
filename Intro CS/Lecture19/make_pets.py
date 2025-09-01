# Write the function according to this spec
def make_pets(d):
    """ d is a dict mapping a Person obj to a Cat obj
    Prints, on each line, the name of a person, 
    a colon, and the name of that person's cat """
    # your code here


p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(1)
c2.set_name("fluffsphere")

# d = {p1:c1, p2:c2}
# make_pets(d)  # prints ana:furball
       #        james:fluffsphere