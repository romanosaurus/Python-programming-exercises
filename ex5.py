'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class ExerciseFive:
    def getString(self):
        inpt = input('give your string:')
        return inpt

    def printString(self, str):
        print(str.upper())

ex = ExerciseFive()
res = ex.getString()
ex.printString(res)