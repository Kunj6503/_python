class BaseClass:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
class ChildClass(BaseClass):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def User (self):
        print( f"My name is : {self.name} and my surname is : {self.surname}")


name = input("Enter your name : ")
surname = input("Enter your surname : ")
person = ChildClass(name,surname)
person.User()