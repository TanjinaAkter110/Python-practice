def finance_tracker (transactions, budget):
    budget= float (input('Enter your monthly budget'))
    transactions= ["Amount", "Categories", "Type"]
    for transaction in transactions:
        if transaction== "Amount":
            Amount= float (input('Enter your transaction amount or done'))
            if Amount.lower== "done":
                print ("Your monthly finance has been calculated")
                break
        if transaction== "Catergories":
            Catergories= str(input('Enter category'))
        if  transaction== "Type":
            Type= str (input('Enter type (income/expense)'))

            total_income= 0
            total_expense= 0
        
            if Type=='income':
                income= float(income.replace("income", ""))
                total_income= total_income+ income
                print ('Total incomes:', total_income )
            if Type== 'expense':
                expense= float(expense.replace("expense", ""))
                total_expense= total_expense+ expense
                print ('Total expenses:', total_expense)

        Net_balance= total_income- total_expense
        print ('Net balance:', Net_balance)
        print ("Financial_status:")
        if Net_balance> budget:
            print ("Surplus")
        
        elif budget-0.05 <= Net_balance <= budget + 0.05:
            print ('Balanced')
        
        elif Net_balance<budget:
            print ('Deficit')
        if 'Financial_status'== 'Deficit':
            Over_budget= budget-Net_balance
            percentage_over= (Over_budget/budget)*100
            


