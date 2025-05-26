# square root with negative flag

guess = 0
neg_flag = False
x = int(input("Enter a positive integer: "))
if x < 0:
    neg_flag = True
while guess**2 < x:
    guess = guess + 1
if guess**2 == x:
    print(f'Square root of {x} is {guess}')
else:
    print(f'{x} is not a perfect square')
    if neg_flag:
        print(f'Just checking... did you mean {-x} ?')