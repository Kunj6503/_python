class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
        
person = employee("kunj",21)
print(person)
# print(person.name)
# print(person.age)