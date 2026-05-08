
from categories import categorize_expense
from reports import monthly_summary, frequent_provider

FILE_NAME = "expenses.txt"

def add_expense():
    provider = input("Enter provider/pharmacy/store name: ")
    amount = float(input("Enter amount spent: "))
    date = input("Enter date (YYYY-MM-DD): ")

    category = categorize_expense(provider)

    with open(FILE_NAME, "a") as file:
        file.write(f"{provider},{category},{amount},{date}\n")

    print("\nExpense saved successfully!")
    print(f"Category: {category}")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

            if not expenses:
                print("No expenses found.")
                return

            print("\n=== All Healthcare Expenses ===")
            for expense in expenses:
                provider, category, amount, date = expense.strip().split(",")
                print(f"{date} | {provider} | {category} | ${amount}")

    except FileNotFoundError:
        print("No expense file found.")

def main():
    while True:
        print("\n==== SnapSpend Health ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Most Frequent Provider")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary(FILE_NAME)
        elif choice == "4":
            frequent_provider(FILE_NAME)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
