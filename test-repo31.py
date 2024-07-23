# Write a Python program to find the maximum of three numbers.

first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
third = int(input("Enter your third number: "))

# display the input
print("The Maximum number is", end=" ")

# solution to the problem.
if second <= first >= third:
    print(first)
elif first <= second >= third:
    print(second)
elif first <= third >= second:
    print(third)