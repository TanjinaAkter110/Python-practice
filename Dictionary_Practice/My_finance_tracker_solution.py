print ("Welcome to finance tracker application")
print ("Let's track your spending today!")
total_monthly_saving= float(input(" Enter your monthly desired savings: "))

finance_array= []
while True:
    transactions= input("Enter your transaction amount/type done: ")
    if transactions=="done":
        break
    Category= input ("Enter your transation category: ")
    Type= input ("Enter your transaction type income/expense: ")


    finance_dictionary= {
        "transactions": float(transactions),
        "Category": Category,
        "Type": Type
                        
    }
    finance_array.append(finance_dictionary)

total_income= 0
total_expense= 0
for finance in finance_array:
    if finance ['Type'] == 'income':
        total_income= total_income+ finance['transactions']
    if finance ['Type']== 'expense':
        total_expense= total_expense+ finance ['transactions']

balance= total_income-total_expense

print ("--------Finacial_report--------")
print ("Total income is:", total_income)
print ("Total expense is:", total_expense)
print ("Net_balance is:", balance)

Highest_spending_category= "" 
Highest_spending_percentage= 0
First_array = finance_array[0]
transaction_value= First_array ['transactions']
Lowest_spending_category= ""


for finance in finance_array:
    if finance ['Type']== 'expense':
        print ("-", finance ['Category'])
        percentage= (finance['transactions']/ total_expense)*100
        print("{:.2f}%".format(percentage))
        if percentage >30:
            
            print ("Warning! you have spend more than 30% in this category ")
    
            
        if Highest_spending_percentage < percentage:
            Highest_spending_percentage= percentage
            Highest_spending_category= finance ['Category'] 
        if transaction_value > percentage:
            transaction_value=percentage
            Lowest_spending_category= finance ['Category']

print ('Highest spending category is:',Highest_spending_category ) 
print ('Lowest spending percentage is:', Lowest_spending_category)

if balance> total_monthly_saving:
    print ("Surplus")  
elif total_monthly_saving-0.05 <= balance <= total_monthly_saving + 0.05:
    print ('Balanced')
else:
    print ("Deficit") 

