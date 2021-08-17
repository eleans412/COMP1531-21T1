# Prompt the user for input
weight = input("What is your weight in kg? ")
height = input("What is your height in m? ")

# Convert string to integer
weight = float(weight)
height = float(height)

# Calculate BMI
BMI = weight/(height*height)
BMI = round(BMI, 1)

print("Your BMI is", BMI)