#fast square root using bisection search

x = 54321  # try 0.5
epsilon = 0.01
num_guesses = 0
low = 0.0
high = x
guess = (high + low)/2

while abs(guess**2 - x) >= epsilon:
    print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print(f'num_guesses = {str(num_guesses)}')
print(f'{str(guess)} is close to square root of {str(x)}')