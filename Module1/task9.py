a = int(input("enter the length of the array : "))

numbers = []

for i in range(a):
    num = int(input("Enter the number in the array : "))
    numbers.append(num)

negative = []
for j in range(len(numbers)):
    if numbers[j]>0:
        sum = 0
        sum = sum + numbers[j]
        #sum = numbers[j]+numbers[++j]
    #elif numbers[j]<0:
    else:
        sum2 =  numbers[j]+numbers[++j]
        

print("Sum of all positive numbers is : ",sum)
print("Sum of all negative numbers is : ",sum2)