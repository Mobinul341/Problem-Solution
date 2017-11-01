''' #1st problem
a = float(input("Enter a number:"))
b = float(input("Enter a number:"))
print("Addition: ", eval(str(a + b)),
      "\nSubtraction: ", eval(str(a - b)),
      "\nMultiplication: ", eval(str(a * b)),
      "\nQuotient: ", eval(str(a / b)),
      "\nReminder: ", eval(str(a % b)))
'''
'''
#2nd problem
from math import pi
r = float(input("Enter Radius: "))
def circumference():
    cir = 2*pi*r
    print("This is Circumference", cir)
def area():
    ar = pi*r**2
    print("This is area: ", ar)

circumference()
area()

'''
'''
#3rd problem

a = float(input("Enter value of A:"))
b = float(input("Enter value of B:"))
x = ((3.14*a**2 + 2.01*b**3)/ (7.01*b**2 + 2.01*a**3))
print("Result of Equation is: ", eval(str(x)))
'''

#4th problem
x = int(input("Enter value of X:"))
y = int(input("Enter value of Y:"))

def incre(x,y):
    while x>=y:
        print(x)

        x-=1






incre(x,y)




