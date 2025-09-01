import random

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

class Rabbit(Animal):
    """ A subclass of Animal """
    def speak(self):
        """ prints the string meep to the console """
        print('meep')
    def __str__(self):
        """ Repr as "rabbit", a colon, its name, a colon, its age """
        return "rabbit:"+str(self.get_name())+":"+str(self.get_age())
   
c = Rabbit(5)
print(c)
c.speak()
c.set_name('fluffy')
print(c)