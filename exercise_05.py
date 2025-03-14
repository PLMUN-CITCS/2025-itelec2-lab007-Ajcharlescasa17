import math  # Import math module

# Get numerical input from the user
user_number = float(input("Enter a number to perform operations on: "))

# Perform arithmetic operations
addition = user_number + 10
subtraction = user_number - 5
multiplication = user_number * 2
division = user_number / 3

# Use math library functions
if user_number >= 0:
    sqrt_value = f"{math.sqrt(user_number):.2f}"
else:
    sqrt_value = "Undefined"

sine_value = f"{math.sin(math.radians(user_number)):.4f}"  # Convert degrees to radians for sine calculation

# Display the results with exact formatting
print("Enter a number to perform operations on:")
print("\nArithmetic Operations:")
print(f"User number + 10 = {addition:.2f}")
print(f"User number - 5  = {subtraction:.2f}")
print(f"User number * 2  = {multiplication:.2f}")
print(f"User number / 3  = {division:.2f}")

print("\nMath Library Functions:")
print(f"Square root of {user_number:.2f} is: {sqrt_value}")
print(f"Sine of {user_number:.2f} degrees is: {sine_value}")