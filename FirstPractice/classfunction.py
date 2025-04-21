class People:

    def height(h):
        return h + 2
    def weight(w):
        return w+5
    def color(c):
        return c

class Animal:
    def height(h):
        return h + 14

HeightAfterOneYear = People.height(150) #152
HeightAfterOneYearForAnimal = Animal.height(150) # 164
print(HeightAfterOneYear)
print(HeightAfterOneYearForAnimal)



def grade(number):
    if (number > 80):
        grade = "A plus"
    elif(number > 70):
        grade = "A"
    elif(number>60):
        grade = "B"
    else:
        grade= "F"
    
    return grade
print ("grade of student:", grade(60))