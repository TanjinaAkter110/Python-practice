print ("Welcome to the personal_finance_tracker!")
print ("Let`s track your spending today!")
total_income= float(input("Enter your salary"))
total_budget= float( input("Enter your monthly budget"))

items= []
amounts= []
print ("Start adding your item")
print ("Type 'done' when you are finished")

while True:
    item= input ("Where do you want to spend?")
    if item.lower()== "done":
        print ("All the items has been added successfully")
        break
    amount_input= float(input("Enter the amount"))

cost= float(amount_input)
items.append (item)
amounts.append(cost)
total_spending= sum(amounts)

highest_percentage= 0
highest_spend_item= ""
for i in range (len(items)):
    percentage= (amounts[i]/total_spending)*100
    print(f"{items[i]}: {round(percentage, 2)}%")
    if percentage>30:
        print(f"Warning! You spent a lot on {items[i]}! That's more than 30%!")
    if percentage> highest_percentage:
        highest_percentage= percentage
        highest_spend_item= item [i]
print ("Highest spending category:", highest_spend_item)

net_balance= (total_income-total_spending)

if net_balance>total_budget:
    print ("Surplus")
        
elif total_budget-0.05 <= net_balance <= total_budget + 0.05:
    print ('Balanced')
        
elif net_balance<total_budget:
    print ('Deficit')



