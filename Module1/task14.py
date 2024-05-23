tuple = ("kunj","rekha","srushti","ragho")
print("This is your tuple : " ,tuple)

try:
    num = input("enter the name to get the index number : ").strip()
    index = tuple.index(num)
    print("the index number of entered name is : " ,index)

except:
    print(num, " is not present in the tuple")