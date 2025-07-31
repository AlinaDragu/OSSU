# Write a function that meets this specification
def count_words(sen):
    """ sen is a string representing a sentence 
    Returns how many words are in sen (i.e. a word is a 
    a sequence of characters between spaces. """
    # your code here
    L1 = sen.split(' ')
    return len(L1)
        

s = "Hello it's me"
print(count_words(s))   # prints 3

s = "I just took a DNA test turns out I'm 100% splitting strings"
print(count_words(s))   # prints 12