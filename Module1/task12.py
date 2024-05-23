tuple = ("kunj","rekha","srushti","ragho")
print("This is your tuple : " ,tuple)

x = ("debanshu",)
tuple += x
print("This is tuple with inserted value : " ,tuple)

print(tuple[0])
print(tuple[-1])

z = int(len(tuple)/2)
print(tuple[z])