a = int(input("enter the length of the array : "))

numbers = []

for i in range(a):
    num = int(input("Enter the number in the array : "))
    numbers.append(num)

total = sum(numbers)

print("The summation of all the numbers is : ",total)