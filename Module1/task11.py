a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))

print("the numbers entered by you are:", a, b, c)

if a > b:
    if a < c:
        small = b
        bich = a
        large = c
    elif b > c:
        small = c
        bich = b
        large = a
    else:
        small = b
        bich = c
        large = a
else:
    if b < c:
        small = a
        bich = b
        large = c
    elif a > c:
        small = c
        bich = a
        large = b
    else:
        small = a
        bich = c
        large = b

print("smallest number =", small)
print("middle number =", bich)
print("largest number =", large)
