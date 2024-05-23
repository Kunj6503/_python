# Take 3 numbers from the user
numbers = []
for i in range(3):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Sort the numbers
numbers.sort()

# Display the largest, smallest, and intermediate numbers
largest = numbers[2]
smallest = numbers[0]
intermediate = numbers[1]

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Intermediate number: {intermediate}")
