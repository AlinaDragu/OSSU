# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon

cube = 27
epsilon = 0.01
low = 0
high = cube

guess = (high+low)/2
while abs(guess**3-cube) > epsilon:
    if guess**3 > cube :
        #guess too high
        high = guess
    else:
        low = guess
    guess = (high+low)/2
    
print(guess)