def numbers (a,b):
    addition= a+b
    return addition
a = int (input('Enter the number='))
b= int (input ('Enter the number'))
addition= numbers (a,b)

def average (a,b):
    average= addition/2
    return average
average= average (a,b)

def area (a,b):
    areaoftriangle= 0.5* (a*b)
    return areaoftriangle
areaoftriangle= area(a,b)

print ('Addition of the number=',addition )
print ('Average of the number=', average)
print ('Area of the triangle=', areaoftriangle)
