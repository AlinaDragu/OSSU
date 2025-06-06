x = 0.5
epsilon = 0.01
# choose the low endpoint
low = 4
# choose the high endpopint
high = 10

guess = (high + low)/2

while abs(guess**2 - x) >= epsilon:
    #print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
print(f'{str(guess)} is close to square root of {str(x)}')