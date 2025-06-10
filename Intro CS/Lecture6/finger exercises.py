# Assume you are given an integer 0 \<= N \\<= 1000. 
# Write a piece of Python code that uses bisection search to guess N.
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N.
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

N = int(input("Enter a number between 0 and 1000: ")) 
low = 0
high = 1000

for count in range(1,21):
    guess = (low + high) // 2
    if guess == N:
        print(f"count: {count}")
        print(f"answer: {guess}")
        break
    elif guess < N:
        low = guess + 1
    else:
        high = guess - 1