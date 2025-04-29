class Calculator:
    def addition (a,b):
        return a+b
    def substraction (a,b):
        return (a-b)
    def multiplication (a,b):
        return (a*b)
    def division (a,b):
        return (a/b)
    
Addition_of_the_numbers= Calculator.addition (5,10)
Substraction_of_the_numbers= Calculator.substraction (10,5)
Multiplication_of_the_numbers= Calculator.multiplication(10,10) 
Division_of_the_numbers= Calculator.division(50,10)

print("Addition:", Addition_of_the_numbers)
print ("Substraction:", Substraction_of_the_numbers)
print ("Multiplication:", Multiplication_of_the_numbers)
print ("Division:", Division_of_the_numbers)