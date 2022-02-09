# Get the loan details

money_owed = float(input("How much money do you owe, in dollars?\n"))  # $50000
apr = float(input("What is annual rate?\n"))  # 3%
payment = float(
    input("What will be your montly payment be, in dollars?\n"))  # 1000
months = int(input("How many months do you want to see results for?\n"))  # 24

# Divide apr by 100 to make it a percent, then divide by 12 to make monthly

monthly_rate = apr / 100 / 12

# Add in interest

interest_paid = money_owed * monthly_rate
money_owed = money_owed + interest_paid
