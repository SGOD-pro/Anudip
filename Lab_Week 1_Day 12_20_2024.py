# Program to find the largest among three numbers using nested if

# Input three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Determine the largest number using nested if
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

# Print the largest number
print("The largest number is:", largest)

# Program to calculate transport fare based on distance travelled

# Input distance travelled
distance = float(input("Enter the distance travelled (in Km): "))

# Calculate the fare based on the distance
if distance <= 50:
    fare = distance * 8
elif distance <= 100:
    fare = (50 * 8) + ((distance - 50) * 10)
else:
    fare = (50 * 8) + (50 * 10) + ((distance - 100) * 12)

# Print the total fare
print("The total fare is: Rs.", fare)