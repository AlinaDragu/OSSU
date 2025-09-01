lass Rabbit(Animal):
    """ A subclass of Animal """
    def speak(self):
        """ prints the string meep to the console """
        print('meep')
    def __str__(self):
        """ Repr as "rabbit", a colon, its name, a colon, its age """
        return "rabbit:"+str(self.get_name())+":"+str(self.get_age())
   
# c = Rabbit(5)
# print(c)
# c.speak()
# c.set_name('fluffy')
# print(c)