### example with returning a tuple with many values
###################
def quotient_and_remainder(x, y):
      q = x // y
      r = x % y
      return (q, r)

# result = quotient_and_remainder(10,3)
# print(result)

(quot, rem) = quotient_and_remainder(5,2)
print('quotient is:', quot)
print('remainder is:', rem)