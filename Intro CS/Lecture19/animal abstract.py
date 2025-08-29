# Animal abstract data type 

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

# #default parameters with methods        
a = Animal(4)
print(a)
b = Animal(6)
print(b)
# print(a.age)
# print(a.get_age())

# a.set_name("fluffy")
# print(a.name)
# print(a.get_name())
# print(a)
# a.set_name()
# print(a)