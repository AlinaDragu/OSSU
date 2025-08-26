# In this problem, you will implement two classes according to the specification below: 
# one Container class and one Queue class (a subclass of Container).   
  
# Our Container class will initialize an empty list. 
# The two methods we will have are to calculate the size of the list and to add an element. 
# The second method will be inherited by the subclass. 
# We now want to create a subclass so that we can add more functionality – the ability to remove elements from the list. 
# A Queue will add elements to the list in the same way, but will behave differently when removing an element.

# A queue is a first-in, first-out data structure. Think of a store checkout queue. 
# The customer who has been in the line the longest gets the next available cashier. 
# When implementing your Queue class, you will have to think about which end of your list contains the element that has been in the list the longest.
# This is the element you will want to remove and return.