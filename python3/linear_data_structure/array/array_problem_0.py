#
#     Let us say your expense for every month are listed below,
#         January - 2200
#         February - 2350
#         March - 2600
#         April - 2130
#         May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


monthly_expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
if monthly_expense[0] < monthly_expense[1]:
    extra = monthly_expense[1] - monthly_expense[0]
    print(f"I spent {extra}$ extra in february compare to january")
else:
    print("I don't spent extra $ in february compare to january")

# 2. Find out your total expense in first quarter (first three months) of the year
total_of_first_quarter = 0
for i in range(3):  # first quarter (first three months)
    total_of_first_quarter += monthly_expense[i]
print(f"Total expense in first quarter (first three months) of the year is {total_of_first_quarter}")

# 3. Find out if you spent exactly 2000 dollars in any month
for expense in monthly_expense:
    if expense == 2000:
        print(f"Yes, I spent exactly 2000 dollars")
        break
else:
    print("No, not spent exactly 2000 dollars in any month")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expense.append(1980)
print("Expenses at the end of June:", monthly_expense)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
monthly_expense[3] += 200
print(monthly_expense)
