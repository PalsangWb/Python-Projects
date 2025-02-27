num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

numbers = [num1, num2, num3]

print(f"Sum: {sum(numbers)}")
print(f"Product: {num1 *num2 * num3}")
print(f"Average: {sum(numbers)/len(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")