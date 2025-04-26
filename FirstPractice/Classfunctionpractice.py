class Walking:
    def distance(d):
        return d/15
    def tired (t):
        if t>10:
            t="Tired"
        else:
            t= "Not tired"
        return t

class Running:
     def distance(d):
        return d/10
     def tired (t):
        if t>25:
            t="Tired"
        else:
            t= "Not tired"
        return t
Target= 15
DistanceGone= Walking.distance(15)   
TiredAmount= Walking.tired (15)  
DistanceGone1= Running.distance(15)
TiredAmount1= Running.tired (15)
print (DistanceGone)
print(TiredAmount)
print(DistanceGone1)
print(TiredAmount1)
