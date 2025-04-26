class People:
    def __init__():
        return "Hi I am a class"
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