from . import Expense
import collections


# Read in the Spending Data
expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

# Create a List of the Spending Categories
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

# Count Categories with a Counter Collection
spending_counter = collections.Counter(spending_categories)
print(spending_counter)

top5 = collections.Counter.most_common(spending_counter, 5)
print(top5)