class Greeting:
    def __init__(self,name,num):
        self.name = name
        self.num = num

    def mf(abc):
        print("Hello my name is : ", abc.name, "and my phone number is : ", abc.num)

name = input("enter you name : ").strip()
num = int(input("enter you phone number : "))

person = Greeting(name,num)
person.mf()