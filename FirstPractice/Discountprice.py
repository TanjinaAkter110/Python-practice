Product= float (input('Enter the price= '))
if Product>100:
    Discount= Product*0.10
    new_price= Product-Discount
    print('After the discount ')
    print(new_price)
          
else:
    print('No discount')