# Modify the str method to represent the Fraction as just the 
# numerator, when the denominator is 1. Otherwise its representation 
# is the numerator then a / then the denominator, as before

class Fraction(object):
    """ A number represented as a fraction """
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Returns a string representation of self """
        # modify this
        if self.denom == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.denom)

 
a = Fraction(1,4)
b = Fraction(3,1)
print(a)     # prints 1/4
print(b)     # prints 3