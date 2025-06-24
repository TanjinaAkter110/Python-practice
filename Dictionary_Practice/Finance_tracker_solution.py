print ("Welcome to the personal_finance_tracker!")
print ("Let`s track your spending today!")
total_budget= float( input("Enter your monthly budget: "))

financeArr = []

while True:
    transaction = input("Enter transaction amount: ")
    if transaction == "done":
        break
    catagory = input("Enter category: ")
    type = input("Enter type (income/expense): ") 

    finacntDict = {
        "transaction" : float(transaction),
        "catagory" : catagory,
        "type" : type
    }
    financeArr.append(finacntDict)

totalIncome = 0
totalExpense = 0

for finance in financeArr:
    if finance['type'] == 'income':
        totalIncome = totalIncome + finance['transaction']
    if finance['type'] ==  'expense':
        totalExpense = totalExpense + finance['transaction']

balance = totalIncome - totalExpense
print ("---FINANCIAL REPORT---")
print ("Total Income: " , totalIncome)
print("Total expense: " , totalExpense)
print ("Net Balance: " , balance)

print("Expense Breakdown:")
highestSpendingCatagory = ""
highestSpendingPercantage = 0 
for finance in financeArr:
    if finance['type'] == 'expense':
        print("- " , finance['catagory'])
        percentage = (finance['transaction'] / totalExpense) * 100
        print(percentage , "%")
        if highestSpendingPercantage < percentage:
            highestSpendingPercantage = percentage
            highestSpendingCatagory = finance['catagory']


print("Highest Spending Category:",  highestSpendingCatagory)

if total_budget < balance:
    print("Financial Status: Surplus")
else:
    print("Financial Status: Deficit")