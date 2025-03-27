MarksAsAStr=input('enter your score ')
Marks=int(MarksAsAStr)
if Marks> 100:
    print('Invalid marks')
elif Marks>=80:
    print('Grade A')
elif Marks>=60:
    print('Grade B')
elif Marks>=40:
    print('Grade C')
else:
    print('Grade F')