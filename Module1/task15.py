tuple = ("kunj","rekha","srushti","ragho")
print("This is your tuple : " ,tuple)


name = input("enter the name to get the index number : ").strip()
    
# found = False
for i in range(len(tuple)):
    if name == tuple[i]:
        print("the index of the name is : " ,i)
        # found=True  
        break   
# if not found:
#     print("not in the tuple")   