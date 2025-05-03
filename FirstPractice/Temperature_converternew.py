def Check_temperature (Value,Unit):
    if Unit=='C':
        C= (Value*9/5)+32
    return C
    if Unit== 'F':
        F= (Value-32)*5/9
    return F

Value= int(input('Enter a value'))
Unit= input ('Choose a Unit between C and F')
Temperature= Check_temperature (Value,Unit)
print ("The temperature is:", Temperature)
