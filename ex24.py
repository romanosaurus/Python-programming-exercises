'''
Python has many built-in functions, and if you do not know how to use it, 
you can read document online or find some books. 
But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
'''

# __doc__ to get manual


def square(x):
    '''
        return the square of a number
    '''
    return x ** 2


print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
print(square.__doc__)
