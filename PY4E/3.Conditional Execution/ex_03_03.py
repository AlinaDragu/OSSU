# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")

try:
    sc = float(score)
    
    if sc < 0.0 or sc > 1.0:
        print("Error:Score is out of range.Enter a value between 0.0 and 1.0")
    elif sc >= 0.9:
        print("A")
    elif sc >= 0.8:
        print("B")
    elif sc >= 0.7:
        print("C")
    elif sc >= 0.6:
        print("D")
    elif sc < 0.6:
        print("F")
        
except:
        print("Error:Invalid input.Please enter a number:")