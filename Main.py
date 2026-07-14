import json

FILENAME = "budget_data.json"

budget = 0.00
expenses = []

def load_data():
    global budget, expenses

    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
            budget = data.get("budget", 0.0)
            expenses = data.get("expenses", [])

    except FileNotFoundError:
        print("No saved data found. Starting new Budget.")

def save_data():
  data = {
      "budget": budget,
      "expenses": expenses
  }

  with open(FILENAME, "w") as file:
    json.dump(data, file)


def set_budget():
    global budget

    while True:
        try:
            value = float(input("Enter budget amount: £"))

            if value <= 0:
                print("Enter a value greater than 0")
            else:
                budget = value
                print(f"Budget set to £{budget:.2f}")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

 
def add_expense():
    global expenses
    
    while True:
        try:
            amount = float(input("Enter expense amount: £"))

            if amount <= 0:
                print("Amount must be greater than 0")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        category = input("Enter category: ")

        if category == "":
            print("Category cannot be blank")
        else:
            break

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    total_expenses = 0

    for item in expenses:
        total_expenses += item["amount"]

    remaining_budget = budget - total_expenses

    print("Expense added successfully")
    print(f"Remaining budget: £{remaining_budget:.2f}")

    if remaining_budget < 0:
        print("ALERT: You have exceeded your budget!")

    elif budget > 0 and remaining_budget <= budget * 0.1:
        print("WARNING: Less than 10% of your budget remaining.")

def display_expenses():

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\nExpenses")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['category']} - £{expense['amount']:.2f}")

def display_balance():
    
    remaining_budget = budget - total_expenses
    
    print(F"Remaining Budget: £{remaining_budget}")  

def display_summary():
     if len(expenses) == 0:
     
    

