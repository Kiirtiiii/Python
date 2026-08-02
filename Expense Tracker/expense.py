import matplotlib.pyplot as plt
expenses = []
from datetime import datetime
def menu():
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search Expense")
    print("5. Monthly Summary")
    print("6. Generate Charts")
    print("7. Exit")
while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("enter amount: rs".title()))
        category = input("enter category:".title())
        note = input("enter note (or type cancel):".title())
        if note.lower() == "cancel":
            continue
        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        while True:
            print("\n expense details".title())
            print(f"amount : Rs {amount}".title())
            print(f"category : {category}".title())
            print(f"note : {note}".title())

            print("\n1. save expense".title())
            print("2. re-enter details".title())
            confirm = input("choose:".title())
            if confirm == "1" :
                expenses.append(expense)
                print("expense added successfully!".title())
                break
            elif confirm == "2" :
                print("re-entering expense...\n".title())
                break
            else :
                print("invalid choice!!".title())
    elif choice == "2":
        if expenses:
            print("\n===== your expense =====".title())
            for i, expense in enumerate(expenses, start=1): 
             print(f"{i}. {expense['date']} | rs {expense['amount']} | {expense['category']} | {expense['note']}".title())
        else :
            print("no expenses found".title())
    elif choice == "3":
        if expenses:
            print("\n===== Delete Expenses =====")
            for i, expense in enumerate (expenses, start=1):
                print(f"{i}. rs {expense['amount']} | {expense['category']} | {expense['note']}".title())
            choice = int(input("\nenter expense number to delete:".title()))
            if 1 <= choice <= len(expenses): 
                    deleted = expenses.pop(choice - 1)
                    print(f"{deleted['category']} expense deleted successfully.".title())
            else:
                    print("invalid expense number.".title())
        else:
            print("no expenses to delete".title())
    elif choice == "4":
        keyword = input("enter category or note to search :").title()
        found = False
        for i, expense in enumerate(expenses, start=1):
            if keyword in expense["category"].title() or keyword in expense["note"].title():
                print(f"{i}. Rs {expense['amount']} | {expense['category']} | {expense['note']}") 
                found = True
            if not found: 
                print("no matching expenses found.".title())
    elif choice == "5":
                total = 0
                category_totals = {}

                for expense in expenses :
                    total += expense["amount"]
                    category = expense["category"]
                    if category in category_totals:
                        category_totals[category] += expense["amount"]
                    else :
                        category_totals[category] = expense["amount"]
                print("\n===== monthly summary =====".title())
                print(f"total expenses: Rs{total}".title())
                print("\ncategory-wise spending:")
                for category, amount in category_totals.items():
                    print(f"{category}: Rs{amount}")
                
    elif choice == "6":
        while True:
            print("\n==== charts ====".title())
            print("1. category-wise bar chart".title())
            print("2. category-wise pie chart".title())
            print("3. back".title())

            chart_choice = int(input("enter your choice:".title()))
            if chart_choice == 1 :
                category_totals = {}
                for expense in expenses:
                    category = expense["category"]
                    if category in category_totals :
                        category_totals[category] += expense["amount"]
                    else :
                        category_totals[category] = expense["amount"]
                plt.bar(category_totals.keys(),category_totals.values())
                plt.title("expenses by category".title())
                plt.xlabel("Category")
                plt.ylabel("Amount (Rs)")
                plt.figure(figsize=(8,5))
                plt.tight_layout()
                plt.savefig("bar_chart.png", dpi=300)
                plt.show()  

            elif chart_choice == 2 :
                category_totals = {}
                for expense in expenses:
                    category = expense["category"]
                    if category in category_totals :
                        category_totals[category] += expense["amount"]
                    else :
                        category_totals[category] = expense["amount"]
                plt.figure(figsize=(7,7))
                plt.pie(
                    category_totals.values(),
                    labels=category_totals.keys(),
                    autopct="%1.1f%%",
                    startangle=90
                )
                plt.title("category-wise expense distribution".title())
                plt.figure(figsize=(8,5))
                plt.tight_layout()
                plt.savefig("pie_chart.png", dpi=300)
                plt.show()


            elif chart_choice == 3 :
                break
            else :
                print("invalid choice".title())
        if not expenses:
            print("no expenses to plot".title())
            continue
        
    elif choice == "7":
        print("goodbye!".title())
        break
    else :
        print("Invalid Choice !!")
    
    