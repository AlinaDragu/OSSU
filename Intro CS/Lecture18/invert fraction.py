# Implement the missing get_inverse and invert methods below
class SimpleFraction(object):
    """ A number represented as a fraction """
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def get_inverse(self):
        """ Returns a float representing 1/self """
        # your code here
        return self.denom/self.num
        
    def invert(self):
        """ Sets self's numerator to its denominator and vice versa.
            Returns None. """
        # your code here
        # newdenom = self.num
        # newnum = self.denom
        # self.num = newnum
        # self.denom = newdenom
        
        #other way
        (self.num,self.denom) = (self.denom,self.num)
        
        
f1 = SimpleFraction(3,4)
print(f1.num, f1.denom)   # prints 3 4 
print(f1.get_inverse())   # prints 1.33333333 (note this one returns value)
f1.invert()               # acts on data attributes internally, no return
print(f1.num, f1.denom)   # prints 4 3 