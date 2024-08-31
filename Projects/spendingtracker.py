def print_menu():
    print("----- Expense Tracker Menu -----")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. View expenses by category")
    print("4. View summary by category")
    print("5. Exit")
    print("--------------------------------")

def add_expense(spending, expense_categories):
    while True:
        category = input(f"Enter the expense category from {expense_categories}: ")
        if category in expense_categories:
            amount = float(input("Enter the amount you spent: "))
            date = input("Enter the date (yyyy-mm-dd): ")
            description = input("Add a brief description or note about the expense: ")
            info = {"Category": category, "Amount": amount, "Date": date, "Description": description}
            spending.append(info)
            again = input("Do you want to add another expense? (yes/no): ")
            if again.lower() != "yes":
                break
        else:
            print("Enter an expense category that exists in the list.")

def main():
    spending = []
    expense_categories = [
        "Food", "Entertainment", "Utilities", "Housing", "Transportation",
        "Health & Fitness", "Personal Care", "Education", "Travel", 
        "Shopping", "Savings & Investments", "Miscellaneous"
    ]
    print("---Welcome to The Spending Tracker---")
    
    while True:
        print_menu()
        choose = input("Choose an option: ")

        if choose == "1":
            add_expense(spending, expense_categories)
        
        elif choose == "2":
            for info in spending:
                print(f"Expense Category: {info['Category']} \nAmount: {info['Amount']} \nDate: {info['Date']} \nDescription: {info['Description']}")
        
        elif choose == "3":
            name = input("Enter the expense category you want to display: ")
            if name in expense_categories:
                for info in spending:
                    if name == info['Category']:
                        print(f"Expense Category: {info['Category']} \nAmount: {info['Amount']} \nDate: {info['Date']} \nDescription: {info['Description']}")
            else:
                print("Enter an expense category that exists in the list.")
        
        elif choose == "4":
            total = 0
            name = input("Enter the expense category you want to summarize: ")
            if name in expense_categories:
                for info in spending:
                    if name == info['Category']:
                        total += info['Amount']
                print(f"Total for {name}: {total}")
            else:
                print("Enter an expense category that exists in the list.")
        
        elif choose == "5":
            print("Exiting...")
            break

        else:
            print("Enter a valid option.")

if __name__ == "__main__":
    main()
