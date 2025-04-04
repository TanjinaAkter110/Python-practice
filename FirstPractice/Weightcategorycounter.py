weightlist = [45, 59, 90, 32, 56, 43, 41, 99, 55, 56, 78, 43, 31, 33, 98]
Countofskinny= 0
Countofhealthy= 0
Countoffat= 0

for weight in weightlist:
   if weight<55:
       Countofskinny= Countofskinny+1

   elif weight<=65:

        Countofhealthy= Countofhealthy+1

   else:
        Countoffat= Countoffat+1

print ('Skinny people:', Countofskinny)
print ('Healthy people:', Countofhealthy)
print ('Fat people:', Countoffat)
    