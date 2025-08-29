# Write a function that meets this spec.

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname


def make_animals(L1, L2):
    """ L1 is a list if ints and L2 is a list of str
        L1 and L2 have the same length
    Creates a list of Animals the same length as L1 and L2.
    An animal object at index i has the age and name
    corresponding to the same index in L1 and L2, respectively. """
    # your code here
    L3 = []
    for i in range(len(L1)):
        # i is 0,1,2,3,4,5
        age = L1[i]
        name = L2[i]
        a = Animal(age)
        a.set_name(name)
        L3.append(a)
    return L3
                


L1 = [2,5,1]
L2 = ["blobfish", "crazyant", "parafox"]
animals = make_animals(L1, L2)
print(animals)     # note this prints a list of animal objects
for i in animals:  # this prints the indivdual animals
    print(i)