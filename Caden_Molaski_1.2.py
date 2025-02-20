num_pennies = float(input("Enter the number of pennies:"))
num_nickels = float(input("Enter the number of nickels:"))
num_dimes = float(input("Enter the number of dimes:"))
num_quarters = float(input("Enter the number of quarters:"))
pennies = 0.01
nickels = 0.05
dimes = 0.10
quarters = 0.25
total_amount = (num_pennies*pennies)+(num_nickels*nickels)+(num_dimes*dimes)+(num_quarters*quarters)
print(f"Total amount: ${total_amount:.2f}")