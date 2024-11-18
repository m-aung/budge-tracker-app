class Expense:
  def __init__(self,description:str,amount:float) -> None:
    self.description = description
    self.amount = amount
    pass

def format_options(choice:str, description:str) -> None:
  print(f'{choice}. {description}')

def show_app_menu(options:list[tuple[str, str]]):
  print('\nWhat would you like to do?')
  for choice, description in options:
    format_options(choice, description)
  
def add_expense(expenses:list[Expense], description:str, amount:float):
  expenses.append(Expense(description, amount))
  print(f'Added expense: {description}\n Amount: ${amount}')

def get_total_expenses(expenses:list[Expense]) -> float:
  sum = 0
  for expense in expenses:
    sum += expense.amount
  return sum

def get_balance(budget:float, expenses:list[Expense]):
  return budget - get_total_expenses(expenses)

def show_budget_details(budget:float, expenses:list[Expense]):
  print(f'Total budget: {budget}')
  print('Expenses:')
  for expense in expenses:
    print(f'- {expense.description}: {expense.amount}')
  print(f'Total Spent: {get_total_expenses(expenses)}')
  print(f'Remaining Budget: {get_balance(budget,expenses)}')

def main():
  print('Welcome to the Budge App')
  starting_balance = float(input('Enter your initial budget: '))

  budget = starting_balance
  expenses:list[Expense] = []
  menu = [('1', 'Add an expense'),('2', 'Show budget details'),('3', 'Exit')]

  # we will repeat always
  while True:
    show_app_menu(menu)
    choice = input(f'Enter your choice ({menu[0][0]}/{menu[1][0]}/{menu[2][0]}): ')
    if choice == menu[0][0]:
      description = input('Enter expense description: ')
      amount = input('Enter expense amount: ')
      
      (expenses, description, amount)
    elif choice == menu[1][0]:
      show_budget_details(budget,expenses)
    elif choice == menu[2][0]:
      print('Exiting the app.\n goodbye')
      break
    else: 
      print('Invalid choice, please try again.')


main()
