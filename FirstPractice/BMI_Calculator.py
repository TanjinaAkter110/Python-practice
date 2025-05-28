def BMI_calculator_with ( w, h):
    BMI= w/(h*h)
    return BMI
w= float (input('Enter your weight in Kg:'))
h=  float (input('Enter your height in meter:'))
BMI= BMI_calculator_with(w,h)


if BMI<18.5:
    print ('Category: Underweight')
elif 18.5 <= BMI <= 24.9: 
    print ('Catergory: Normal')
else:
    print ('Catergory: Overweight')

print ('Your BMI is:', BMI)



   