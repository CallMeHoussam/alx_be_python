income = int(input("Enter your monthly income:"))
expense = int(input("Enter your total monthly expenses:"))
monthly_save = income - expense
print("Your monthly savings are $",monthly_save)
interest_rate = 0.05
Project_saving = monthly_save * 12 + (monthly_save * 12 * interest_rate)
print("Projected savings after one year, with interest, is: $",Project_saving)
