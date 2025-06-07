monthly_budget = float(input("Enter the monthly Budget: "))
total_income= 0
total_expense= 0
highest_spending_amount = 0
highest_spending_category = ""
financial_status = ""
transactionDictionaries = []
balance = 0

while True:
    transaction_catagory = input("Enter Catagory: ")
    if transaction_catagory== "done":
        break
    transaction_amount = float(input("Enter transaction: "))
    transaction_type = input("Enter Type: ")
    transaction = {
        "Amount": transaction_amount,
        "Category": transaction_catagory,
        "Type": transaction_type
    }

    transactionDictionaries.append(transaction)

    if transaction["Type"] == "income":
        total_income = total_income + transaction["Amount"]
        balance = balance + transaction["Amount"]
    if transaction["Type"] == "expense":
        total_expense = total_expense + transaction["Amount"]
        balance = balance - transaction["Amount"]

print("---- Financial Report ----")
print("Total Income: ", total_income)
print("Total Expense: " , total_expense)
print("Net Balance: ", balance)
print("Expense Breakdown: ")


for transactionsD in transactionDictionaries:
    if highest_spending_amount < transactionsD["Amount"]:
        highest_spending_amount = transactionsD["Amount"]
        highest_spending_category = transactionsD["Category"]
    if transactionsD["Category"] == "expense":
        print("- " ,  transactionsD["Category"] ,":" ,  (transactionsD["Amount"]/total_expense)*100, "%")

print("Highest Spending Catagory: ", highest_spending_category)

if balance > monthly_budget:
    financial_status = 'Surplus'

elif (monthly_budget * 0.95) <= balance <= (monthly_budget * 1.05):
    financial_status = 'Balanced'

else:
    financial_status = 'Deficit'

print("Financial Status: ", financial_status)

if financial_status == "Deficit":
    over_budget = monthly_budget - balance
    percent_over = (over_budget / monthly_budget) * 100

    print("Warning: " , highest_spending_category, " exceeds budget by " , percent_over , "%!")



