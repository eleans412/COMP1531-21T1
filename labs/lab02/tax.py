ode # Prompt user input
income = input("Enter your income: ")

# Turn string into float
income = float(income)
# Calculate taxable income
tax = 0
# If bottom
if income <= 18200:
    tax = 0
# If second
elif income >=18201 and income <=37000:
    tax = 0.19 * (income - 18200)
# If third
elif income >=37001 and income <=87000:
    tax = 3572 + 0.3725 * (income - 37000)
# If fourth
elif income >=87001 and income <=180000:
    tax = 19822 + 0.37 * (income - 87000)
# If top
elif income >= 180001:
    tax = 54232 + 0.45 * (income - 180000)

# Format tax to be of dollar value
#formatted_tax = round(tax, 2)

# Print taxable income
print('The estimated tax on your income is $' + '{:,.2f}'.format(tax))