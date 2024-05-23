a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))

print("the number entered by you are : " ,a,b,c)

large = a

if b > large:
    large = b

if c > large:
    large = c

small = a

if b < small:
    small = b

if c < small:
    small = c

bich_ka = a+b+c-large-small

print("smallest number = ", small)
print("bich ka number = ", bich_ka)
print("largest number = ", large)