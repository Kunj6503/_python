# incorrect way

class BaseClass:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
class ChildClass(BaseClass):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def User (self):

        self.name = input("Enter your name : ")
        self.surname = input("Enter your surname : ")

        print( f"My name is : {self.name} and my surname is : {self.surname}")
    
person = ChildClass("name","surname")
person.User()