# EXAMPLE: Exceptions with user input
######################################

def divide_nums1():
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print(a/b)

divide_nums1()


def divide_nums2():
    try:
        a = int(input("Tell me one number: "))
        b = int(input("Tell me another number: "))
        print(a/b)
    except:
        print("Bug in user input")

divide_nums2()


def divide_nums3():
    try:
        a = int(input("Tell me one number: "))
        b = int(input("Tell me another number: "))
        print("a/b = ", a/b)
        print("a+b = ", a+b)
    except ValueError:
        print("Could not convert to a number.")
    except ZeroDivisionError:
        print("Can't divide by zero")
        print("a/b = infinity")
        print("a+b =", a+b)
    except:
        print("Something went very wrong.")
