def track():
    budget = float(input('Irasykite BIUDZETA '))
    expenses = []

    while True:
        expense = float(input('Irasykite islaidas arba 0 kai norite sustoti '))
        if expense == 0:
            break
        else:
            expenses.append(expense)

    total_expenses = sum(expenses)
    balance = budget - total_expenses

    print("\nBudget Summary:")
    print(f"Income: {budget}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Balance: {balance}")


track()