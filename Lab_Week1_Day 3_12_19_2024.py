# 1. Check if the number is even or odd using ternary operator
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number is {result}")

# 2. Swap two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swapping the numbers
a, b = b, a

print(f"After swapping: first number is {a}, second number is {b}")