def grade(number):
    if number>80:
        grade = "A plus"
    elif number>70:
        grade = "A"
       
    elif number>60:
        grade = "A minus"
        
    else:
        grade = "F"
    return grade
print ("Grade of the student:", grade (90))


    