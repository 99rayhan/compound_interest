"""Compute the interest value of a user bank account with the interest rate of 4% per year
 and calculate the total amount of 1,2 and 3 years."""

print("Welcome to 'Nijer Bank LTD'")
print("Your current account balance is: 12565.54 tk")
deposited_balance = 12565.54
#after one year account balance with 4%
interest = 4/100
first_year = deposited_balance*interest
print(f"First year interest is {first_year:.2f} tk.")
first_year_total = first_year+deposited_balance
print(f"First year balance after interest added is {first_year_total:.2f} tk..")

new_deposit = float(input("New deposited value is: "))

new_balance = first_year_total+new_deposit
print(f"New balance is {new_balance:.2f} tk.")

second_year = new_balance*interest
print(f"Second year interest is {second_year:.2f} tk.")

second_year_total = second_year+new_balance
print(f"Second year balance after interest added is {second_year_total:.2f} tk..")

