### EXAMPLE: improved bisection square root as a function
# takes in x and an epsilon
#########################

def bisection_root_new(x, epsilon):
    num_guesses = 0
    low = 0
    high = x
    guess = (high + low)/2.0
    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x: 
            low = guess
        else: 
            high = guess
        guess = (high + low)/2.0
        num_guesses += 1
    print('num_guesses =', num_guesses)
    return guess